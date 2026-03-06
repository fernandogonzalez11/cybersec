from sage.modules.free_module_integer import IntegerLattice

pubkey = Matrix(ZZ, [
    [47, -77, -85],
    [-49, 78, 50],
    [57, -78, 99]
])

c0 = vector([171, -237, -634])

A = pubkey
A2 = A.row(1)
A3 = A.row(2)

Ainv = A.inverse()

print(A2)

# for known plaintext char x
x = ord('H')
t = c0 - x*A.row(0)

B = Matrix([A2, A3])

print(B)

L = IntegerLattice(B.LLL())
print(L)
v = L.closest_vector(t)

r = t - v

print(r)

file = open("output.txt")
for line in file:
    c = vector(eval(line))
    m = (c - r) * Ainv

    print(chr(m[0]), end='')

print()
