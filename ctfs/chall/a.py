a = input().lower()

b = ""

for i in range(len(a)):
    nn = ord(a[i])
    if not (ord('a') <= nn and nn <= ord('z')):
        continue
    else:
        b += a[i]

# print(b)

a = b

def f():
    for i in range(len(a)//2):
        # print(a[i], a[len(a)-i-1])
        if (a[i] != a[len(a)-i-1]): return False

    return True

if f(): print("YES")
else: print("NO")