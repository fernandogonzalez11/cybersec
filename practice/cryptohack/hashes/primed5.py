from Crypto.PublicKey import RSA
from Crypto.Hash import MD5
from Crypto.Signature import pkcs1_15
from Crypto.Util.number import long_to_bytes, bytes_to_long, isPrime
import math
import json
'''
from utils import listener
# from secrets import N, E, D

FLAG = "crypto{??????????????????}"


key = RSA.construct((N, E, D))
sig_scheme = pkcs1_15.new(key)


class Challenge():
    def __init__(self):
        self.before_input = "Primality checking is expensive so I made a service that signs primes, allowing anyone to quickly check if a number is prime\n"

    def challenge(self, msg):
        if "option" not in msg:
            return {"error": "You must send an option to this server."}

        elif msg["option"] == "sign":
            p = int(msg["prime"])
            if p.bit_length() > 1024:
                return {"error": "The prime is too large."}
            if not isPrime(p):
                return {"error": "You must specify a prime."}

            hash = MD5.new(long_to_bytes(p))
            sig = sig_scheme.sign(hash)
            return {"signature": sig.hex()}

        elif msg["option"] == "check":
            p = int(msg["prime"])
            sig = bytes.fromhex(msg["signature"])
            hash = MD5.new(long_to_bytes(p))
            try:
                sig_scheme.verify(hash, sig)
            except ValueError:
                return {"error": "Invalid signature."}

            a = int(msg["a"])
            if a < 1:
                return {"error": "`a` value invalid"}
            if a >= p: # can't be p
                return {"error": "`a` value too large"}
            g = math.gcd(a, p)
            flag_byte = FLAG[:g]
            return {"msg": f"Valid signature. First byte of flag: {flag_byte}"}

        else:
            return {"error": "Unknown option."}


import builtins; builtins.Challenge = Challenge # hack to enable challenge to be run locally, see https://cryptohack.org/faq/#listener
# listener.start_server(port=13392)
'''

# https://crypto.stackexchange.com/questions/105669/quickest-way-to-find-md5-collision
# ig this is cheating lol

# MD5 property:
# if MD5(x) = MD5(y) => MD5(x+z) = MD5(y+z)
# and since MD5 is Merkle Damgard, we can have a length extension attack wherein we concatenate this z value
# given two collisioned hashes, we can bruteforce this z

# https://stackoverflow.com/questions/1756004/can-two-different-strings-generate-the-same-md5-hash-code
x = bytes.fromhex("4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa200a8284bf36e8e4b55b35f427593d849676da0d1555d8360fb5f07fea2")
y = bytes.fromhex("4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa202a8284bf36e8e4b55b35f427593d849676da0d1d55d8360fb5f07fea2")

assert(bytes_to_long(x) < bytes_to_long(y))

z = 1

cnt = 0
while True:
    if cnt%1000000 == 0: print(f'{cnt=}')

    x_app = bytes_to_long(x + long_to_bytes(z))
    y_app = bytes_to_long(y + long_to_bytes(z))

    if isPrime(y_app) and not isPrime(x_app):
        print(f"found!!!!!! {z=}")

        print(json.dumps({
            "option": "sign",
            "prime": y_app
        }))

        print(json.dumps({
            "option": "check",
            "prime": x_app,
            "signature": "???",
            "a": "???" # a factor of x
        }))

        break

    z += 2
    cnt += 1



