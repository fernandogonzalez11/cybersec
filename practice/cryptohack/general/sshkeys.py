from Crypto.PublicKey import RSA

file = "bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub"
data = open(file, encoding="utf-8").read()

key = RSA.import_key(data)