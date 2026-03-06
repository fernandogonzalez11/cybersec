def sqrt(x, p):
    for i in range(0, p):
        if (i*i)%p == x: return i

    return -1

p = 29
ints = [14,6,11]

print([sqrt(x,p) for x in ints])