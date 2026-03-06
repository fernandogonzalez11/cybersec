# ofb attack

# observe: if we know the iv we can know the entire sequence of intermediate values
# steps:
# get iv from encrypt_flag()
# pass encrypt() with that iv, and a long string of \x00
# result will be the sequence of intermediate values (because they're all xored with 0)
# xor each ciphertext block with its corresponding intermediate value

from Crypto.Cipher import AES
import os
from pwn import xor
import requests

KEY = os.urandom(16)
FLAG = "crypto{myveryeryerylongstringgggggggggggggggggggggggggggggggggg}"

sesh = requests.Session()
BASE_URL = "https://aes.cryptohack.org/symmetry/"

#@chal.route('/symmetry/encrypt/<plaintext>/<iv>/')
def encrypt(plaintext, iv):
    plaintext = bytes.fromhex(plaintext)
    iv = bytes.fromhex(iv)
    if len(iv) != 16:
        return {"error": "IV length must be 16"}

    cipher = AES.new(KEY, AES.MODE_OFB, iv)
    encrypted = cipher.encrypt(plaintext)
    ciphertext = encrypted.hex()

    return {"ciphertext": ciphertext}


#@chal.route('/symmetry/encrypt_flag/')
def encrypt_flag():
    iv = os.urandom(16)

    cipher = AES.new(KEY, AES.MODE_OFB, iv)
    encrypted = cipher.encrypt(FLAG.encode())
    ciphertext = iv.hex() + encrypted.hex()

    return {"ciphertext": ciphertext}

# API calls:
def encrypt(plaintext, iv):
    return sesh.get(BASE_URL + f"encrypt/{plaintext}/{iv}/") \
        .json()

def encrypt_flag():
    return sesh.get(BASE_URL + "encrypt_flag") \
        .json()


enc = encrypt_flag()["ciphertext"]

iv = enc[:16*2]
cipher = enc[16*2:]

sequence = encrypt("00" * 64, iv)["ciphertext"]

print(xor(bytes.fromhex(sequence), bytes.fromhex(cipher)))