#!/usr/bin/env python3

import hashlib
from Crypto.Util.number import long_to_bytes

FLAG = b"crypto{???????????????????????}"
PRIME = 77793805322526801978326005188088213205424384389488111175220421173086192558047


def _eval_at(poly, x, prime):
    accum = 0
    for coeff in reversed(poly):
        accum *= x
        accum += coeff
        accum %= prime
    return accum


def make_deterministic_shares(minimum, shares, secret, prime):
    if minimum > shares:
        raise ValueError("Pool secret would be irrecoverable.")

    coefs = [secret]
    for i in range(1, shares + 1):
        coef = hashlib.sha256(coefs[i-1]).digest()
        coefs.append(coef)
    coefs = [int.from_bytes(p, 'big') for p in coefs]
    poly = coefs[:minimum]

    points = []
    for i in range(1, shares + 1):
        point = _eval_at(poly, coefs[i], prime)
        points.append((coefs[i], point))

    return points


# shares = make_deterministic_shares(minimum=3, shares=7, secret=FLAG, prime=PRIME)
# for share in shares:
#     print(share)


# i get the (hash(secret), point)

# h1, h2, h3
coefs = [105622578433921694608307153620094961853014843078655463551374559727541051964080]
points = [25953768581962402292961757951905849014581503184926092726593265745485300657424]

coefs = [long_to_bytes(p) for p in coefs]
for i in range(2):
    coef = hashlib.sha256(coefs[i-1]).digest()
    coefs.append(coef)

coefs = [int.from_bytes(p, 'big') for p in coefs]
h1,h2,h3 = coefs

print(coefs)

secret = (points[0] - (h2*coefs[0] + h1)*coefs[0]) % PRIME
print(long_to_bytes(secret))