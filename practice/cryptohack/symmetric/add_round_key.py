state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    n = len(s)
    assert(len(k) == n)
    
    for i in range(n):
        for j in range(n):
            s[i][j] ^= k[i][j]

    return s

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return b''.join([bytes(row) for row in matrix])

print(add_round_key(state, round_key))
print(matrix2bytes(state))
