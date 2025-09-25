from math import gcd
import freq

with open('input.txt') as f:
    s = f.read()

sz = 5
n = len(s)

spacings = []

for i in range(0, n-sz+1):
    p = s[i:i+sz]
    for j in range(i+sz, n-sz+1):
        q = s[j:j+sz]
        if (p == q):
            spacings.append((p, j-i))
            break

print(spacings)

g = 1

if (len(spacings) > 0):
    g = spacings[0][1]
    for i in range(1, len(spacings)):
        g = gcd(g, spacings[i][1])

    print(g)

g = 3
print(g)

subciphers = []

print("analyze:")
for i in range(0, g):
    p = s[i::g]
    print(f"T{i}", end=': ')
    print(p)

    subciphers.append(p)

print("=====")
for i, p in enumerate(subciphers):
    print(f"+++ T{i} +++")
    freqs, chars = freq.analyze(p)

    for f in freqs:
        perc = f[0] / chars * 100
        print(f"{f[1]} {perc:.2f}")

def ceasar_match(num: int, origin: str, dest: str):
    global s

    dif = ord(dest) - ord(origin)

    changed = list(s)

    for i in range(num, n, g):
        val = ord(s[i]) - ord('A')
        val += dif
        val %= 26
        val += ord('a')
        changed[i] = chr(val)

    s = ''.join(changed)
    print(s)
    print()

print("=====")
print(s)
print()
ceasar_match(0, 'E', 'E')
ceasar_match(1, 'R', 'E')
ceasar_match(2, 'H', 'E')