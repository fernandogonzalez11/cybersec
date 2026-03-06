# openssl pkey -pubin -in transparency_afff0345c6f99bf80eab5895458d8eab.pem -outform DER | openssl sha256

from Crypto.PublicKey import RSA
import hashlib

file = "transparency_afff0345c6f99bf80eab5895458d8eab.pem"
data = open(file, encoding="utf-8").read()

key = RSA.import_key(data).public_key()
der = key.export_key(format="DER")

# key fingerprint is the hash of the key in its DER representation
sha256 = hashlib.sha256(der)
fingerprint = sha256.hexdigest()

print(fingerprint)


"""
openssl pkey -pubin -in transparency_afff0345c6f99bf80eab5895458d8eab.pem -outform DER | openssl sha256
SHA2-256(stdin)= 29ab37df0a4e4d252f0cf12ad854bede59038fdd9cd652cbc5c222edd26d77d2

plug in crt.sh > advanced > search by identity sha256
"""

"""
important to remember that the fingerprint is from the DER!!!!! representation
"""