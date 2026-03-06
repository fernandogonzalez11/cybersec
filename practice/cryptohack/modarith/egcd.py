def egcd(a, b):
    if b == 0: return (1, 0)

    x1, y1 = egcd(b, a % b)
    x = y1
    y = x1 - y1 * (a//b)

    return (x, y)

print(egcd(26513, 32321))
print(egcd(12,6))