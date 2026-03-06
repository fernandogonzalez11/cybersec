from Crypto.Util.number import getPrime, inverse, bytes_to_long
import random
import math

FLAG = b'crypto{?????????????????????}'

flag_test1 = b'crypto{!!!!!!!!!!!!!!!!!!!!!}'
flag_test2 = b'crypto{~~~~~~~~~~~~~~~~~~~~~}'

# https://blog.cloudflare.com/lattice-crypto-primer/

def gen_key():
    q = getPrime(512)
    upper_bound = int(math.sqrt(q // 2))
    lower_bound = int(math.sqrt(q // 4))
    f = random.randint(2, upper_bound)
    while True:
        g = random.randint(lower_bound, upper_bound)
        if math.gcd(f, g) == 1:
            break
    h = (inverse(f, q)*g) % q
    print(f'{h.bit_length()=}')

    return (q, h), (f, g)


def encrypt(q, h, m):
    assert m < int(math.sqrt(q // 2))
    print(f'{m.bit_length()=}')
    r = random.randint(2, int(math.sqrt(q // 2)))
    e = (r*h + m) % q
    rhq = (r*h)%q
    print(f'{rhq.bit_length()=}')
    print(f'{e.bit_length()=}')
    return e


def decrypt(q, h, f, g, e):
    a = (f*e) % q
    m = (a*inverse(f, g)) % g
    return m


public, private = gen_key()
q, h = public
f, g = private

m = bytes_to_long(FLAG)
e = encrypt(q, h, m)

print(f'Public key: {(q,h)}')
print(f'Encrypted Flag: {e}')

m1 = bytes_to_long(flag_test1)
m2 = bytes_to_long(flag_test2)
r1 = ((e-m1)%q * inverse(h,q)) % q
r2 = ((e-m2)%q * inverse(h,q)) % q
print(r1, r2, r2-r1, (r2-r1).bit_length())