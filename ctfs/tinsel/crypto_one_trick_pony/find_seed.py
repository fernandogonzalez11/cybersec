X_BITS = 500
PARTITIONS = int(input("partitions: "))
WORKER_ID = int(input("worker id: ")) # 1 indexed

#################################
# 34 bit prime
p_rng = 14519419643
# from factor.py
x = 1527177990631697490769938740356122521290237679801547397044344173466127856428713302030373391531980498813820455049638404511681636177235400142365828358686
#################################

START = (p_rng//PARTITIONS) * (WORKER_ID-1)
STOP = (p_rng//PARTITIONS) * WORKER_ID + 2*X_BITS
print(f"starting from {START}")
print(f"ending at {STOP}")

W = x
MASK = (1 << X_BITS) - 1

# build sliding window
cur = 0
for i in range(1, X_BITS + 1):
    cur = (cur << 1) | int(pow(START + i, (p_rng - 1)//2, p_rng) == 1)

for s in range(START + X_BITS, STOP):
    if s%10000000==0: print(s)

    nxt = s + 1
    if nxt % p_rng == 0: nxt = 1

    if cur == W:
        print("BIG WIN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("prime:", p_rng)
        print("original seed:", nxt-X_BITS)
        print("next seed value:", nxt)

        break

    cur = ((cur << 1) & MASK) | int(pow(nxt, (p_rng - 1)//2, p_rng) == 1)

else:
    print("[-] seed not found")
