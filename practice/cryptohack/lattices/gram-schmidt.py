import numpy as np

def norm2(v): return np.dot(v, v)

def ortho_basis(basis: list):
    sz = basis[0].size
    ortho = [basis[0]]
    for i in range(1, len(basis)):
        oi = basis[i].astype(np.float64)
        for j in range(0, i):
            mu = np.dot(basis[i], (1 / norm2(ortho[j])) * ortho[j])
            oi -= mu*ortho[j]

        ortho.append(oi)

    return ortho


v = [
    np.array([4,1,3,-1]),
    np.array([2,1,-3,4]),
    np.array([1,0,-2,7]),
    np.array([6,2,9,-5])
]

print(ortho_basis(v))
