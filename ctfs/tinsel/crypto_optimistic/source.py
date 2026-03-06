import string, re, random, hashlib
from secret import STARSHARD_SCROLL, SECRET, PEPPERMINT_KEYWORD
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES

# obs: len(ALPHABET) = len(L)
SECRET = re.sub(r'[^a-zA-Z0-9]', '', SECRET).upper()
ALPHABET = string.ascii_uppercase + string.digits
SZ = 6
L = SZ**2

def weave_peppermint_square():
    peppermint_square_flat = ALPHABET
    for c in PEPPERMINT_KEYWORD:
        peppermint_square_flat = peppermint_square_flat.replace(c, '')
    peppermint_square_flat = PEPPERMINT_KEYWORD + peppermint_square_flat
    return [list(peppermint_square_flat[i:i+SZ]) for i in range(0, len(peppermint_square_flat), SZ)]

peppermint_square = weave_peppermint_square()

COORDS = {
    peppermint_square[i][j]: f'{i+1}{j+1}'
    for j in range(SZ)
    for i in range(SZ)
}

def swirl_encrypt(key, plaintext):
    twinkling_ct = []
    for i in range(len(plaintext)):
        key_off = int(COORDS[key[i % len(key)]])
        pt_off = int(COORDS[plaintext[i]])
        twinkling_ct.append(key_off + pt_off)
    return twinkling_ct


# key is 36 chars!!
STARSTREAM_KEY = ''.join(random.sample(ALPHABET, k=L))
PEPPERMINT_CIPHERTEXT = swirl_encrypt(STARSTREAM_KEY, SECRET)

COCOA_AES_KEY = hashlib.sha256(SECRET.encode()).digest()
# ecb!!!
WRAPPED_STARSHARD = AES.new(COCOA_AES_KEY, AES.MODE_ECB).encrypt(pad(STARSHARD_SCROLL, 16)).hex()

open('output.txt', 'w').write(f'{PEPPERMINT_KEYWORD = }\n{PEPPERMINT_CIPHERTEXT = }\n{WRAPPED_STARSHARD = }')