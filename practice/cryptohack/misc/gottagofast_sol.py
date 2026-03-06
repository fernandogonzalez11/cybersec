from pwn import *
import time
from json import dumps, loads
from Crypto.Util.number import long_to_bytes

conn = connect("socket.cryptohack.org", 13372)

def generate_key(t):
    key = long_to_bytes(t)
    return hashlib.sha256(key).digest()

def decrypt(c, key):
    c = bytes.fromhex(c)
    assert len(c) <= len(key), "Data package too large to encrypt"
    plaintext = b''
    for i in range(len(c)):
        plaintext += bytes([c[i] ^ key[i]])
    return plaintext

def send_json(obj):
    conn.sendline(dumps(obj).encode())

def recv_json():
    return loads(conn.recvline())

current_time = int(time.time())

print(conn.recvline())

send_json({"option": "get_flag"})
info = recv_json()

enc = info["encrypted_flag"]

for i in range(10):
    key = generate_key(current_time+i)
    print(decrypt(enc, key))