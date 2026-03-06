# find_seed_fixed.py
X_BITS = 500
PARTITIONS = int(input("partitions: "))
WORKER_ID = int(input("worker id: "))  # 1-indexed

# RNG parameters (known)
p_rng = 14529203489
x = 1380844581695640772438661954974177510082545059352213361588806990936174075582263279114693681118011292298710376264483980232484553331506609556766839998049

FLAG = open("flag.txt").read()
TARGET_BITS = len(FLAG) * 8

# ----- helpers -----
def norm(z):
    z %= p_rng
    return 1 if z == 0 else z

def bit(z):
    return int(pow(norm(z), (p_rng - 1) // 2, p_rng) == 1)

# ----- segmentation (with backward overlap) -----
chunk = p_rng // PARTITIONS
RAW_START = chunk * (WORKER_ID - 1)
RAW_STOP  = chunk * WORKER_ID

START = max(0, RAW_START - X_BITS)          # backward overlap
STOP  = min(p_rng, RAW_STOP + 2 * X_BITS)   # forward safety

print(f"searching seeds in [{START}, {STOP})")

# ----- build initial window -----
MASK = (1 << X_BITS) - 1
cur = 0
for i in range(X_BITS):
    cur = (cur << 1) | bit(START + i)

# ----- slide -----
for s in range(START, STOP - X_BITS):
    if s % 10_000_000 == 0:
        print(s)

    if cur == x:
        nxt = norm(s + X_BITS)
        print("BIG WIN")
        print("prime:", p_rng)
        print("original seed:", nxt-X_BITS)
        print("next seed value:", nxt)

        print(f"next {TARGET_BITS} bits:", end=" ")
        z = nxt
        for _ in range(TARGET_BITS):
            print(bit(z), end="")
            z = norm(z + 1)
        print()
        break

    # slide window
    cur = ((cur << 1) & MASK) | bit(s + X_BITS)

else:
    print("[-] seed not found")
