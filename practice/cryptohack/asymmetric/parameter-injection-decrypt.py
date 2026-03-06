from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import bytes_to_long
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


shared_A = "0xada6e8c5d0d210488e4c38fa2185badc1e6805da39c86869d4fe72e10a9e33af8972599a729654bab8bc72af00c108dc7934d1586719f1e8f6c3b95843b6c7e39e1a5a156e5e341d7bbb050d45783a48b241bc1bb658ae584e60e1b096b5dec0cfe1fbd9a2894f1f52e85848dd7f8d3ff8187639ffa40fd743fca87116058fb9285900f42e646adfb46356f95e54f5449aef06eb40e3bc6ab6633452807cd0baf4c7f83c647ac1ddd58b203b585bbd21ba5640d58912dbe6da7647f4c14b503a"
shared_secret = bytes_to_long(bytes.fromhex(shared_A[2:]))

iv = "c3b8a927cb7e1c34b033a5233a6f234e"
ciphertext = "66719031c09a2c50ebae5a6f6ce0047df6517ff4b720127d964071379efd3447"

print(decrypt_flag(shared_secret, iv, ciphertext))

# crypto{n1c3_0n3_m4ll0ry!!!!!!!!}