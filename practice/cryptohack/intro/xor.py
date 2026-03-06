shift = 13
s = "label"

r = [chr(ord(c) ^ shift) for c in s]
print(''.join(r))