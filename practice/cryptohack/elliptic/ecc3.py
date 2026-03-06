a = 497
b = 1768
p = 9739

O = (-1, -1)

def inv(a, n):
    return pow(a, n-1-1, n)

def add(P: tuple, Q: tuple) -> tuple:
    x1, y1 = P
    x2, y2 = Q

    if P == (-1, -1): return Q
    if Q == (-1, -1): return P
    if x1 == x2 and (y1 + y2) % p == 0: return O

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

def mult(P: tuple, n: int) -> tuple:
    if n == 0: return O

    val = mult(P, n//2)
    val = add(val, val)
    if n % 2 != 0: val = add(val, P)

    return val


Qa = (815, 3190)
nb = 1829

key = mult(Qa, nb)

from hashlib import sha1
hash = sha1(str(key[0]).encode()).hexdigest()

print(f'crypto{{{hash}}}')