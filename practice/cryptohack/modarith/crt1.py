def egcd(a, b):
    if b == 0: return (1, 0)

    x1, y1 = egcd(b, a%b)
    x = y1
    y = x1 - y1 * (a//b)
    return (x, y)

# chinese remainder theorem for 2 conditions
# a = a1 mod m1
# a = a2 mod m2
# where m1, m2 are coprime
def crt2(cond1, cond2):
    a1, m1 = cond1
    a2, m2 = cond2

    n1, n2 = egcd(m1, m2)
    a = (a1*n2*m2 + a2*n1*m1) % (m1*m2)
    return a

# chinese remainder theorem for n conditions
# inductive approach
def crt(*conds):
    a = crt2(conds[0], conds[1])
    n = conds[0][1] * conds[1][1]
    for i in range(2,len(conds)):
        a = crt2((a, n), conds[i])
        n *= conds[i][1]

    return a

print(crt(
    (2,3),
    (3,5),
    (2,7)
))
