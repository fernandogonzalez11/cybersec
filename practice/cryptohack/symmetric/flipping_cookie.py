from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad, unpad
from datetime import datetime, timedelta
from pwn import xor
import requests

sesh = requests.Session()
BASE_URL = "https://aes.cryptohack.org/"

KEY = os.urandom(16)
FLAG = "crypto{nice}"


# decrypt with CBC
def check_admin(cookie, iv):
    """
    cookie = bytes.fromhex(cookie)
    iv = bytes.fromhex(iv)

    try:
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(cookie)
        unpadded = unpad(decrypted, 16)
    except ValueError as e:
        return {"error": str(e)}

    print(unpadded)

    if b"admin=True" in unpadded.split(b";"):
        return {"flag": FLAG}
    else:
        return {"error": "Only admin can read the flag"}
    """

    url = BASE_URL + f"/flipping_cookie/check_admin/{cookie}/{iv}/"
    res = sesh.get(url)
    return res.json()

# encrypt with CBC, return iv+enc
def get_cookie():
    """
    expires_at = (datetime.today() + timedelta(days=1)).strftime("%s")
    cookie = f"admin=False;expiry={expires_at}".encode()

    iv = os.urandom(16)
    padded = pad(cookie, 16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(padded)
    ciphertext = iv.hex() + encrypted.hex()

    return {"cookie": ciphertext}
    """

    url = BASE_URL + "/flipping_cookie/get_cookie/"
    res = sesh.get(url)
    return res.json()

enc = get_cookie()["cookie"]
iv = enc[:16*2]
cookie = enc[16*2:]

print(check_admin(cookie, iv))

# https://crypto.stackexchange.com/questions/3654/malleability-attacks-against-encryption-without-authentication
# if I replace ciphertext block N-1 with A ⊕ B ⊕ (ciphertext block N-1) I will have the message B for the plain text block N

A = "admin=False;expi"
B = "admin=True;;expi"

iv = xor(bytes.fromhex(iv), A.encode(), B.encode()).hex()

print(iv)

print(check_admin(cookie, iv))