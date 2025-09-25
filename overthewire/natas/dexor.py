import base64

nums = [30,102,36,7,10,51,39,14,22,55,32,0,23,32,117,85,71,42,56,77,73,102,53,8,6,43,59,0,23,102,109,77,70,37,53,12,84,118,100,77,24,220]

s = '{"showpassword":"no","bgcolor":"#abc123"}'

key = "eDWo"

def encrypt(arr):
	dc = ""
	for i in range(len(arr)):
		n = ord(arr[i]) ^ ord(key[i % len(key)])
		dc += chr(n)
		
	return dc
		
ec = encrypt(s)
ecB = ec.encode('utf-8')
ecB = base64.b64encode(ecB)
ecB = ecB.decode('utf-8')
print(ecB)
