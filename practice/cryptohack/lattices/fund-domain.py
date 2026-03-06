import numpy as np

basis_vectors = np.array([
    [6,2,-3],
    [5,1,4],
    [2,7,1]
])

vol = abs(np.linalg.det(basis_vectors))
print(vol)