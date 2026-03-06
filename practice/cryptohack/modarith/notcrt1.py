# list of tuples (ai, ni) st x === ai mod ni
def notcrt(conds: list):
    a0, n0 = conds[0]
    a1, n1 = conds[1]
    a2, n2 = conds[2]
    k = 0

    while ((n0*k+a0) % n1 != a1): k += 1
    in1 = n0*k+a0
    step = n0*n1
    while (in1 % n2 != a2): in1 += step

    return in1

conds = [
    (2, 5),
    (3, 11),
    (5, 17)
]

print(notcrt(conds))

