import numpy as np
from Crypto.Util.number import isPrime

# prime digs: 53 (5)
# prime upper: 67; 71; 73; 79; 83; 89; (C, G, I, O, S, Y)
# prime lower: 97; 101; 103; 107; 109; 113 (a, g, k, m, q)

# 5Ca
# n = np.int64(53*67*97)
nums = np.array([53,67,101]) # wow, it worked
extra = 71

n1 = nums.sum()
n2 = nums.prod()

s = np.int64(0)
m = np.int64(1)
# 77 7296161743021880191 True

k = 1

while True:
    if k%int(1e7)==0: print(k)

    s += n1
    m *= n2

    if isPrime(int(s+extra)) and isPrime(int(m*extra)): 
        print("sol:", k)
        break

    k += 1

st = '{"password": "' + ''.join([chr(int(x)) for x in nums]) * k + chr(extra) + '"}'
print(st, len(st))

# {"password": "5Ce5Ce5Ce5Ce5Ce5Ce5Ce5Ce5Ce5Ce5Ce5Ce5Ce5Ce5Ce5CeG"}