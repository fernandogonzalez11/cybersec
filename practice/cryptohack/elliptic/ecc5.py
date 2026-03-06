# Elliptic curve in Montgomery form:
# By² = x³ + Ax² + x mod p
# (as opposed from Weierstrass form)

from tonelli import tonelli

a = 486662
b = 1
p = (1<<255) - 19

O = (-1, -1)

# G.x = 9
G = (9, -1)
n = 0x1337c0decafe

def inv(a, n):
    return pow(a, n-1-1, n)

def add(P: tuple, Q: tuple) -> tuple:
    assert(P != Q)

    if P == O: return Q
    if Q == O: return P

    x1, y1 = P
    x2, y2 = Q

    alpha = ((y2-y1) * inv(x2-x1, p)) % p
    x3 = (b*(alpha**2)- a - x1-x2) % p
    y3 = (alpha*(x1-x3) - y1) % p

    return (x3, y3)

def double(P: tuple) -> tuple:
    if P == O: return O

    x1, y1 = P

    alpha = ((3*(x1**2)+ 2*a*x1 + 1) * inv(2*b*y1, p)) % p
    x3 = (b*(alpha**2)- a - 2*x1) % p
    y3 = (alpha*(x1-x3) - y1) % p
    
    return (x3, y3)

def leftmost_pos(n: int) -> int:
    if n == 0: return 0
    i = 0
    while n > 0:
        n >>= 1
        i += 1

    return i-1


def mult(P: tuple, n: int) -> tuple:
    if n == 0: return O

    val = mult(P, n//2)
    val = double(val)
    if n % 2 != 0: val = add(val, P)

    return val

# mult based on the bit representation of n
def mult_montgomery(P: tuple, n: int) -> tuple:
    R = [P, double(P)]

    u = leftmost_pos(n)

    for i in range(u-1, -1, -1):
        S = add(R[0], R[1])
        if n & (1<<i) == 0:
            R = [double(R[0]), S]
        else:
            R = [S, double(R[1])]

    return R[0]
            

# print(p%4) # 1

calc = (pow(G[0],3,p) + a*pow(G[0],2,p) + G[0]) % p
G = (G[0], tonelli(calc, p))

# print(G)
# print(calc == pow(G[1],2,p))

Q = mult(G, n)
print(f'normal mult: crypto{{{Q[0]}}}')

Q = mult_montgomery(G, n)
print(f'mult montgomery: crypto{{{Q[0]}}}')
