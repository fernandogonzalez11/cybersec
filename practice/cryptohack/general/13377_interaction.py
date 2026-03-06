#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs
import random
from pwn import *
import json


class Challenge():
    def __init__(self):
        self.r = remote('socket.cryptohack.org', 13377, level = 'debug')

    def json_recv(self):
        line = self.r.recvline()
        return json.loads(line.decode())

    def json_send(self, hsh):
        request = json.dumps(hsh).encode()
        self.r.sendline(request)

    def do_level(self, json: dict):
        encoding, enc = json["type"], json["encoded"]

        if encoding == "base64":
            encoded = base64.b64decode(enc).decode() # wow so decode
        elif encoding == "hex":
            encoded = bytes.fromhex(enc).decode()
        elif encoding == "rot13":
            encoded = codecs.decode(enc, 'rot_13')
        elif encoding == "bigint":
            # int(enc, 16) -> parse int from str, when its on base 16 (hex format 0xabcde123)
            encoded = long_to_bytes(int(enc, 16)).decode()
        elif encoding == "utf-8":
            encoded = ''.join([chr(b) for b in enc])

        return {"decoded": encoded}

    #
    # This challenge function is called on your input, which must be JSON
    # encoded
    #
    def challenge(self):
        for i in range(100):
            json = self.json_recv()
            
            print(i+1, json)
            if "error" in json: break

            ans = self.do_level(json)
            self.json_send(ans)

        final = self.json_recv()
        print(final)

chall = Challenge()
chall.challenge()

