from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
import numpy as np

public = (7638232120454925879231554234011842347641017888219021175304217358715878636183252433454896490677496516149889316745664606749499241420160898019203925115292257, 2163268902194560093843693572170199707501787797497998463462129592239973581462651622978282637513865274199374452805292639586264791317439029535926401109074800)
enc = 5605696495253720664142881956908624307570671858477482119657436163663663844731169035682344974286379049123733356009125671924280312532755241162267269123486523

q, h = public

def norm2(v): return np.dot(v, v)

def reduce(v1, v2):
    while True:
        if norm2(v2) < norm2(v1):
            v1, v2 = v2, v1

        m = round(np.dot(v1, v2) / norm2(v1))
        if m == 0: return v1, v2

        v2 -= m * v1

def decrypt(q, h, f, g, e):
    a = (f*e) % q
    m = (a*inverse(f, g)) % g
    return m

basis = [
    np.array([1, h]),
    np.array([0, -q])
]

reduced = reduce(*basis)

# reduced[0] is shortest vector -> assumed to be the private key
f, g = reduced[0]

print(reduced)

dec = decrypt(q, h, f, g, enc)

print(long_to_bytes(dec))

# extra:

basis = np.float64(basis)

# 7.63823212045484e+153, 512
vol = abs(np.linalg.det(basis))
print(vol, int(vol).bit_length())