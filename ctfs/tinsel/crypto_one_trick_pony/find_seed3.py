X_BITS = 500
PARTITIONS = int(input("partitions: "))
TRANSITION = 5000  # bits before and after worker boundary

# RNG prime (34-bit)
p_rng = 14519419643
x = 1527177990631697490769938740356122521290237679801547397044344173466127856428713302030373391531980498813820455049638404511681636177235400142365828358686

FLAG = open("flag.txt").read()
MASK = (1 << X_BITS) - 1

# generate boundaries between workers
boundaries = [(p_rng // PARTITIONS) * i for i in range(PARTITIONS)]

# scan each transition
for i in range(PARTITIONS):
    b = boundaries[i]

    # determine start and stop for the window
    start = b - TRANSITION
    stop = b + TRANSITION

    # special handling for cyclic transition at the end
    if i == PARTITIONS - 1:  # last worker -> first
        print(f"scanning cyclic transition around boundary {b}")
        window = [(p_rng - TRANSITION + k) % p_rng or 1 for k in range(2*TRANSITION)]
    else:
        print(f"scanning transition around boundary {b}")
        # make sure start >= 1
        start = max(1, start)
        window = list(range(start, stop))

    # build initial sliding window
    cur = 0
    for j in range(1, X_BITS + 1):
        val = window[j-1] if j-1 < len(window) else window[-1] + (j - len(window))
        if val % p_rng == 0: val = 1
        cur = (cur << 1) | int(pow(val, (p_rng - 1)//2, p_rng) == 1)

    # scan sliding window
    for idx in range(X_BITS, len(window)):
        nxt = window[idx]
        if nxt % p_rng == 0: nxt = 1

        if cur == x:
            print("BIG WIN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("next seed value:", nxt)
            print(f"next {len(FLAG)*8} bits:", end=" ")
            for j in range(nxt, nxt + len(FLAG)*8):
                if j % p_rng == 0: j = 1
                print(int(pow(j, (p_rng - 1)//2, p_rng) == 1), end="")
            print()
            break

        cur = ((cur << 1) & MASK) | int(pow(nxt, (p_rng - 1)//2, p_rng) == 1)
    else:
        print(f"[-] seed not found in transition {i+1}")

