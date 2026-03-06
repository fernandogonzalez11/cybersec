import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def decrypt_flag(ciphertext: str, shared_secret: int, iv: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    iv = bytes.fromhex(iv)
    ciphertext = bytes.fromhex(ciphertext)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    return plaintext

if __name__ == "__main__":
    key_x = 171172176587165701252669133307091694084
    msg = {
        'iv': '07e2628b590095a5e332d397b8a59aa7',
        'encrypted_flag': '8220b7c47b36777a737f5ef9caa2814cf20c1c1ef496ec21a9b4833da24a008d0870d3ac3a6ad80065c138a2ed6136af'
    }

    print(decrypt_flag(msg['encrypted_flag'], key_x, msg['iv']))