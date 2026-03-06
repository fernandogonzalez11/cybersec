from Crypto.PublicKey import RSA

data = open("privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem").read()

key = RSA.import_key(data)

print(key.d)