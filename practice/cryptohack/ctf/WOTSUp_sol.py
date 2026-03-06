import hashlib
import json
from os import urandom
from Crypto.Cipher import AES

BYTE_MAX = 255
KEY_LEN = 32

class Winternitz:
    def __init__(self, priv_seed=urandom(KEY_LEN)):
        self.priv_key = []
        for _ in range(KEY_LEN):
            priv_seed = self.hash(priv_seed)
            self.priv_key.append(priv_seed)
        self.gen_pubkey()

    def gen_pubkey(self):
        self.pub_key = []
        for i in range(KEY_LEN):
            pub_item = self.hash(self.priv_key[i])
            for _ in range(BYTE_MAX):
                pub_item = self.hash(pub_item)
            self.pub_key.append(pub_item)

    def hash(self, data):
        return hashlib.sha256(data).digest()

    def sign(self, data):
        data_hash = self.hash(data)
        data_hash_bytes = bytearray(data_hash)
        sig = []
        for i in range(KEY_LEN):
            sig_item = self.priv_key[i]
            int_val = data_hash_bytes[i]
            hash_iters = BYTE_MAX - int_val
            print(f"{i}: i will hash {hash_iters} times")
            for _ in range(hash_iters):
                sig_item = self.hash(sig_item)
            sig.append(sig_item)
        return sig

    def verify(self, signature, data):
        data_hash = self.hash(data)
        data_hash_bytes = bytearray(data_hash)
        verify = []
        for i in range(KEY_LEN):
            verify_item = signature[i]
            hash_iters = data_hash_bytes[i] + 1
            for _ in range(hash_iters):
                verify_item = self.hash(verify_item)
            verify.append(verify_item)
        return self.pub_key == verify

w = Winternitz()

message1 = b"WOTS Up???"
message2 = b"Sign for flag"

w.sign(message1)

priv_key = [bytes.fromhex("d19f78bdeab019962b2106763862c37ee878e8470f12965a556281d339f9dfab")]
for i in range(KEY_LEN-1):
    priv_key.append(w.hash(priv_key[-1]))

w.priv_key = priv_key
w.gen_pubkey()

signature2 = w.sign(message2)
assert w.verify(signature2, message2)

aes_key = bytes([s[0] for s in signature2])

aes_iv = bytes.fromhex("271c153fa02be81b2685690d8173c36e")
cipher = AES.new(aes_key, AES.MODE_CBC, aes_iv)
enc = bytes.fromhex("0d1fccdab460670b32c32fc60806a0606e01c1707f2b282647b51f2126d8fd6f")
dec = cipher.decrypt(enc)
print(dec)
