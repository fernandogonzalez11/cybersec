def binexpmod(n, e, m):
    if e == 0: return 1

    v = binexpmod(n, e//2, m)
    v *= v
    if e % 2 == 1: v *= n

    return v % m
    
g = 3
m = 13

print(binexpmod(g, m-2, m))