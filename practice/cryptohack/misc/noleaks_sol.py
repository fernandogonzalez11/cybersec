from pwn import *
import base64
from json import dumps, loads

FLAG = "crypto{iamthewalrus}"

# conn = connect("socket.cryptohack.org", 13370)
conn = connect("localhost", 13370)

possible = set(range(0,256))

p = [possible.copy() for _ in FLAG]
p[0] = {ord('c')}
p[1] = {ord('r')}
p[2] = {ord('y')}
p[3] = {ord('p')}
p[4] = {ord('t')}
p[5] = {ord('o')}
p[6] = {ord('{')}
p[-1] = {ord('}')}

def check():
    return all(len(s) == 1 for s in p)

def send_json(obj):
    conn.sendline(dumps(obj).encode())

def recv_json():
    return loads(conn.recvline())

print(conn.recvline())

reqs = 0

while not check():
    send_json({"msg":"request"})
    reqs += 1
    print(reqs, info := recv_json())
    if "error" not in info:
        ciphertext = base64.b64decode(info["ciphertext"])
        for i in range(len(ciphertext)):
            if ciphertext[i] not in p[i]: continue
            p[i].remove(ciphertext[i])

for s in p:
    c = chr(list(s)[0])
    print(c, end='')

print()

print(f"{reqs=}")