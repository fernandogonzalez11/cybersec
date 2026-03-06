def binexpmod(n, e, m):
    if e == 0: return 1

    v = binexpmod(n, e//2, m)
    v *= v
    if e % 2 == 1: v *= n

    return v % m
    
print(binexpmod(3,17,17))
print(binexpmod(5,17,17))
print(binexpmod(7,16,17))
print(binexpmod(273246787654, 65536, 65537))