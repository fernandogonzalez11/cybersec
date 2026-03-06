from Crypto.Util.number import inverse

def egcd(a, b):
    if b == 0: return (1, 0)

    x1, y1 = egcd(b, a%b)
    x = y1
    y = x1 - y1 * (a//b)

    return (x, y)

def inv(a, p):
    return egcd(a, p)[0]

nums = [588,665,216,113,642,4,836,114,851,492,819,237]

for p in range(100, 1000):
    x = (nums[1] * inv(nums[0], p)) % p

    check = (nums[1] * x) % p
    if check == nums[2]: print(f"found: {p=}, {x=}")
