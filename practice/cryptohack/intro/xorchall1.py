# FLAG ^ KEY1 ^ KEY3 ^ KEY2
str1 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
# KEY2 ^ KEY3
str2 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
# KEY1
str3 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"

b1 = bytes.fromhex(str1)
b2 = bytes.fromhex(str2)
b3 = bytes.fromhex(str3)

def bytesxor(b1, b2):
    b3 = [(c1^c2) for c1,c2 in zip(b1,b2)]
    return bytes(b3)

b4 = bytesxor(b1, b2)
b5 = bytesxor(b4, b3)

print(b5)