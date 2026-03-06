import string, re, random, hashlib

ALPHABET = string.ascii_uppercase + string.digits
KEYWORD = 'AR4ND0MK3Y'
SZ = 6
L = SZ**2

def weave_peppermint_square():
    peppermint_square_flat = ALPHABET
    for c in KEYWORD:
        peppermint_square_flat = peppermint_square_flat.replace(c, '')
    peppermint_square_flat = KEYWORD + peppermint_square_flat
    return [list(peppermint_square_flat[i:i+SZ]) for i in range(0, len(peppermint_square_flat), SZ)]

peppermint_square = weave_peppermint_square()
# print(peppermint_square)

COORDS = {
    peppermint_square[i][j]: f'{i+1}{j+1}'
    for j in range(SZ)
    for i in range(SZ)
}

print(COORDS)


chars = [60, 56, 111, 35, 78, 71]

possible = []
for i in range(len(ALPHABET)):
    for j in range(len(ALPHABET)):
        # key + plaintext
        possible.append(int(COORDS[ALPHABET[i]]) + int(COORDS[ALPHABET[j]]))

# possible = [int(COORDS[keyc])+int(COORDS[ptc]) for keyc in ALPHABET for ptc in ALPHABET]

print(len(possible), len(set(possible)))

def possiblechars(char: int):
    chs = []
    for i in range(len(possible)):
        if possible[i] == chars[0]:
            chs.append((ALPHABET[i//len(ALPHABET)], ALPHABET[i%len(ALPHABET)]))

    return chs

chs0 = possiblechars(chars[0])
# chs1 = possiblechars(chars[1])
# chs2 = possiblechars(chars[2])

print(chs0)

# for ch0 in chs0:
#     for ch1 in chs1:
#         for ch2 in chs2:
#             print(ch0[1]+ch1[1]+ch2[1], "with key", ch0[0]+ch1[0]+ch2[0])