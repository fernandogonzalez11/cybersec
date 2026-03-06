from Crypto.Cipher import AES
import os
from pwn import xor
import requests

KEY = os.urandom(16)
sesh = requests.Session()
BASE_URL =  "https://aes.cryptohack.org/bean_counter/"

class StepUpCounter(object):
    def __init__(self, step_up=False):
        self.value = os.urandom(16).hex()
        self.step = 1
        self.stup = step_up

    def increment(self):
        if self.stup:
            self.newIV = hex(int(self.value, 16) + self.step)
        else:
            # oops! typo. step <-> stup
            # since stup=False here, self.value will never change
            self.newIV = hex(int(self.value, 16) - self.stup)
        self.value = self.newIV[2:len(self.newIV)]
        return bytes.fromhex(self.value.zfill(32))

    def __repr__(self):
        self.increment()
        return self.value



#@chal.route('/bean_counter/encrypt/')
def encrypt():
    cipher = AES.new(KEY, AES.MODE_ECB)
    ctr = StepUpCounter()

    print("note: used ctr.value:", ctr.value)

    out = []
    with open("challenge_files/bean_flag.png", 'rb') as f:
        block = f.read(16)
        while block:
            keystream = cipher.encrypt(ctr.increment())

            print("note: used keystream:", keystream.hex())

            xored = [a^b for a, b in zip(block, keystream)]
            out.append(bytes(xored).hex())
            block = f.read(16)

    return {"encrypted": ''.join(out)}

def encrypt():
    return sesh.get(BASE_URL + "encrypt") \
        .json()

# 8950 4e47 0d0a 1a0a 0000 000d 4948 4452
png_first_16_bytes = bytes.fromhex("89504E470D0A1A0A0000000D49484452")

enc = encrypt()["encrypted"]
first_block = enc[:16*2]

ctr_value = xor(png_first_16_bytes, bytes.fromhex(first_block))

# same!!!
print("ctr_value:", ctr_value.hex())

png_contents = xor(ctr_value, bytes.fromhex(enc))
with open("result.png", "wb") as f: f.write(png_contents)