import numpy as np

def norm2(v): return np.dot(v, v)

def reduce(v1, v2):
    while True:
        if norm2(v2) < norm2(v1):
            v1, v2 = v2, v1

        m = round(np.dot(v1, v2) / norm2(v1))
        if m == 0: return v1, v2

        v2 -= m * v1

v=np.array([846835985,9834798552])
u=np.array([87502093,123094980])

reduced = reduce(v, u)

print(np.dot(*reduced))