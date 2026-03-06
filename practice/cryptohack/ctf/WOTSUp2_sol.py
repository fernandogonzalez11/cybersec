from json import loads, dumps
import hashlib
import json
from os import urandom
from Crypto.Cipher import AES

def hash(data):
    return hashlib.sha256(data).digest()

with open("ctf/WOTSUp2_data.json") as f:
    data = loads(f.read())

msg = hash("6df32bef41a3a6242af1702da255d01baf84ebcf9a6a310d8ca90760c0579f28 sent 999999 WOTScoins to me".encode())
signature2 = []

build = [(None, None) for _ in msg]

for sample in data["signatures"]:
    sample_msg = hash(sample["message"].encode())
    sample_sig = sample["signature"]

    for i in range(len(msg)):
        if build[i][0] != None: continue
        if sample_msg[i] >= msg[i]:
            build[i] = (sample_sig[i], sample_msg[i])

print(build)

for i in range(len(msg)):
    dif = build[i][1] - msg[i]

    h = bytes.fromhex(build[i][0])
    for _ in range(dif): h = hash(h)
    signature2.append(h)

aes_key = bytes([s[0] for s in signature2])
aes_iv = bytes.fromhex(data["iv"])
cipher = AES.new(aes_key, AES.MODE_CBC, aes_iv)
enc = bytes.fromhex(data["enc"])
dec = cipher.decrypt(enc)

print(dec)
