from decrypt import decrypt_flag

a = 497
b = 1768
p = 9739

O = (-1, -1)
G = (1804, 5368)

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

Qa_x = 4726
nb = 6534

eq = (pow(Qa_x,3,p) + a*Qa_x + b) % p

# since p = 3 mod 4, sqrt(eq) = eq^((p+1)/4) mod p
Qa_y = pow(eq, (p+1)//4, p)
Qa = (Qa_x, Qa_y)
key = mult(Qa, nb)

msg = {
    'iv': 'cd9da9f1c60925922377ea952afc212c',
    'encrypted_flag': 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'
} 

flag = decrypt_flag(key[0], msg["iv"], msg["encrypted_flag"])
print(flag)
