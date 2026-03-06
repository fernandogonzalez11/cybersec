"""
encrypt "00": 
2c87c5e0281b46742c2eb85b2c9f23c082d21e3b5ecce9e2aede98aa5aaec620
64 bytes (key is <64 bytes)
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import requests
import string

CHUNK_SIZE = 16

KEY = get_random_bytes(CHUNK_SIZE)
FLAG = "crypto{myveryeryerylongstringgggggggggggggggggggggggggggggggggg}"

URL = "https://aes.cryptohack.org/ecb_oracle/encrypt/"
sesh = requests.Session()

# website functionality:
"""
def encrypt(plaintext):
    plaintext = bytes.fromhex(plaintext)

    padded = pad(plaintext + FLAG.encode(), 16)
    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        encrypted = cipher.encrypt(padded)
    except ValueError as e:
        return {"error": str(e)}

    return {"ciphertext": encrypted.hex()}
"""

# API call:
def encrypt(plaintext):
    res = sesh.get(URL + plaintext)
    return res.json()

FLAG_LEN = 64

# get chunk of the hex string
def get_chunk(e, i):
    return e[(i*CHUNK_SIZE*2):((i+1)*CHUNK_SIZE*2)]

def crack():
    guess = [0 for i in range(FLAG_LEN + FLAG_LEN - 1)]
    cracked = ""
    for i in range(FLAG_LEN):
        for c in string.printable:
            i = ord(c)
            guess[FLAG_LEN - 1] = i
            s = bytes(guess).hex()

            # print("plaintext:")
            # arr = [s[i:i+CHUNK_SIZE*2] for i in range(0, len(s), CHUNK_SIZE*2)]
            # print('\n'.join(arr))

            e = encrypt(s)["ciphertext"]
            
            # print("ciphertext:")
            # arr = [e[i:i+CHUNK_SIZE*2] for i in range(0, len(e), CHUNK_SIZE*2)]
            # print('\n'.join(arr))

            if get_chunk(e, 3) == get_chunk(e, 7):
                cracked += c
                print(cracked)
                guess = guess[1:]
                break       

crack()