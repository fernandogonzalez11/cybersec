import string

A = Matrix(ZZ, [
    [47, -77, -85],
    [-49, 78, 50],
    [57, -78, 99]
])
Ainv = A.inverse()

tuples = []
difs = []

f = open("output.txt")
for line in f: 
    tuples.append(vector(eval(line)))

for i in range(1, len(tuples)):
    dif = tuples[i]-tuples[i-1]
    mdif = dif * Ainv
    difs.append(mdif)

print(difs)

for ch in string.ascii_letters:
    print(ch, end='')

    for dif in difs:
        newc = ord(ch) + dif[0]
        if newc < 0 or newc >= 0x110000: break
        ch = chr(newc)
        print(ch, end='')
    print()