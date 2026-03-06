a = 497
b = 1768
p = 9739

# O = (-1, -1)

def inv(a, n):
    return pow(a, n-1-1, n)

def add(P: tuple, Q: tuple) -> tuple:
    x1, y1 = P
    x2, y2 = Q

    if P == (-1, -1): return Q
    if Q == (-1, -1): return P
    if x1 == x2 and (y1 + y2) % p == 0: return (-1, -1)

    if P == Q:
        u1 = (3 * x1 * x1 + a) % p
        u2 = (2 * y1) % p
        l = (u1 * inv(u2, p)) % p
    else:
        u1 = (y2 - y1) % p
        u2 = (x2 - x1) % p
        l = (u1 * inv(u2, p)) % p

    x3 = (l * l - x1 - x2) % p
    y3 = (l * (x1 - x3) - y1) % p
    return (x3, y3)

# X=(5274,2841)
# Y=(8669,740)

# print(addpoints(X,X))


P=(493,5564)
Q=(1539,4742)
R=(4403,5202)

A = add(P, P)
B = add(A, Q)
C = add(B, R)
print(f'crypto{{{C[0]},{C[1]}}}')