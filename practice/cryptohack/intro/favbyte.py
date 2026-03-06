from pwn import xor

str = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

b = bytes.fromhex(str)

for i in range(0, 256):
    print(xor(b, i))