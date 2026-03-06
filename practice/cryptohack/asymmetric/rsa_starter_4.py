p = 857504083339712752489993810777
q = 1029224947942998075080348647219 

N = p*q
phi = (p-1)*(q-1)

def egcd(a, b):
    if b == 0: return (1, 0)
    X1, Y1 = egcd(b, a % b)
    X = Y1
    Y = X1 - (a//b) * Y1
    return (X, Y)

e = 65537
# inverse of e mod phi
d, _ = egcd(e, phi)
print(d)