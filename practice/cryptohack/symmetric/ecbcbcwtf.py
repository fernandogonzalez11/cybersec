from Crypto.Cipher import AES
import os
from pwn import xor
import requests

FLAG = "crypto{myveryeryerylongstringgggggggggggggggggggggggggggggggggg}"
KEY = os.urandom(16)

BLOCK_SIZE = 16

sesh = requests.Session()
url = "https://aes.cryptohack.org/ecbcbcwtf/"

# decrypt in ECB

def decrypt(ciphertext):
    """
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}
    """

    res = sesh.get(url + "decrypt/" + ciphertext)
    return res.json()

# encrypt in CBC
def encrypt_flag():
    """
    iv = os.urandom(16)

    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(FLAG.encode())
    ciphertext = iv.hex() + encrypted.hex()

    return {"ciphertext": ciphertext}
    """

    res = sesh.get(url + "encrypt_flag/")
    return res.json()

# proof of concept
"""
enc = encrypt_flag()
print(enc)
enc = enc["ciphertext"]

last_block = enc[-32:]
before_last_block = enc[-64:-32]

last_block_dec = decrypt(last_block)["plaintext"]

print(xor(bytes.fromhex(last_block_dec), bytes.fromhex(before_last_block)))
"""

# iv + enc
enc = encrypt_flag()["ciphertext"]
n = BLOCK_SIZE*2
enc_l = [enc[i:i+n] for i in range(0, len(enc), n)]

dec = decrypt(enc)["plaintext"]
dec_l = [dec[i:i+n] for i in range(0, len(dec), n)]

msg = [None for i in range(len(enc_l)-1)]

print(enc_l)
print(dec_l)


"""
enc_l: [iv, b1, b2, b3, b4]
dec_l: [_,  b1, b2, b3, b4]
                        i+1
msg:   [m1, m2, m3, m4]
                    i
"""

for i in range(len(msg)-1, -1, -1):
    # aka dec block i with enc block i-1
    msg[i] = xor(bytes.fromhex(dec_l[i+1]), bytes.fromhex(enc_l[i]))


print(b''.join(msg))
