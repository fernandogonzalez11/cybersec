# https://aes.cryptohack.org/ctrime/

from Crypto.Cipher import AES
from Crypto.Util import Counter
import zlib
from string import printable
import os
import requests

WINDOW_SIZE = (1 << zlib.MAX_WBITS)

flag = "crypto{test}"
recovered = ""

known = b"crypto{"

def get_cipher():
    KEY = os.urandom(16)
    iv = int.from_bytes(os.urandom(16), 'big')
    cipher = AES.new(KEY, AES.MODE_CTR, counter=Counter.new(128, initial_value=iv))

    return cipher

cipher = get_cipher()
sesh = requests.Session()

def get_length(payload: bytes):
    url = "https://aes.cryptohack.org/ctrime/encrypt/"
    url += payload.hex()

    res = sesh.get(url).json()
    return len(res["ciphertext"])
    

def get_length_mock(payload: bytes):
    payload += flag.encode()
    data = zlib.compress(payload)
    enc = cipher.encrypt(data)
    return len(enc)

for _ in range(64):          # max remaining length
    best = None
    best_c = None

    for c in printable.encode():
        guess = known + bytes([c])
        l = get_length(guess*32)
        if best is None or l < best:
            best = l
            best_c = c

    known += bytes([best_c])
    print(known)


print(recovered)
