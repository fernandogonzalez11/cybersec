"""
$ nc socket.cryptohack.org 13379
Intercepted from Alice: {"supported": ["DH1536", "DH1024", "DH512", "DH256", "DH128", "DH64"]}
Send to Bob: {"supported":["DH64"]}
Intercepted from Bob: {"chosen": "DH64"}
Send to Alice: {"chosen": "DH64"}
Intercepted from Alice: {"p": "0xde26ab651b92a129", "g": "0x2", "A": "0x742927747122566c"}
Intercepted from Bob: {"B": "0x3184c53d182a53f7"}
Intercepted from Alice: {"iv": "87d1167fb7fe6aaf44c7bfc2350e0453", "encrypted_flag": "ad54d86292bb8232ee7a02ce17cb554d51b1c0fa86e8dd8fa415071bcf2e34d7"}
"""

from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Cipher import AES
# from sage.all import *

p = bytes_to_long(bytes.fromhex("0xde26ab651b92a129"[2:]))
g = 2
A = bytes_to_long(bytes.fromhex("0x742927747122566c"[2:]))
B = bytes_to_long(bytes.fromhex("0x3184c53d182a53f7"[2:]))


# print(p)

# g = Integer(g)
# print(discrete_log(g**Integer(12345), g, Integer(p))) # works
# print(discrete_log(A, g, Integer(p)))


# python -m discretelog 2 8370264763512542828 16007670376277647657

# 5542467534455430744

a = 5542467534455430744
secret = pow(B, a, p)

print(secret) # 7544435797996016442

msg = {
    "iv": "87d1167fb7fe6aaf44c7bfc2350e0453",
    "encrypted_flag": "ad54d86292bb8232ee7a02ce17cb554d51b1c0fa86e8dd8fa415071bcf2e34d7"
}
