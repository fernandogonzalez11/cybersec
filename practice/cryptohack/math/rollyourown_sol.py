from Crypto.Util.number import getPrime
import random

''' test:
q = getPrime(512)
x = random.randint(2, q)

n = q*q
g = 1+q

assert g < n
assert pow(g,q,n) == 1

h = pow(g, x, n)
print(h)

x_sol = (h-1)//q
print(x_sol, x_sol == x)
'''

from pwn import *
from json import dumps

conn = remote('socket.cryptohack.org', 13403)

print(data := conn.recvline())
q = int(data.split(b'"')[1].decode(), 16)

n = q*q
g = 1+q

print(conn.recvuntil(b': '))
conn.sendline(dumps({ "g": hex(g), "n": hex(n) }).encode())

print(data := conn.recvline())
h = int(data.split(b'"')[1].decode(), 16)
print(conn.recvuntil(b': '))

x = (h-1)//q
conn.sendline(dumps({"x": hex(x)}).encode())

print(data := conn.recvline())

# b'{"flag": "crypto{Grabbing_Flags_with_Pascal_Paillier}"}\n'
# https://en.wikipedia.org/wiki/Paillier_cryptosystem
# what lol