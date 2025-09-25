from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# https://en.wikipedia.org/wiki/Linear_congruential_generator
# https://ctftime.org/writeup/12035
# https://hackmd.io/@SBK6401/rkmxfRvao
# https://crypto.stackexchange.com/questions/20495/how-brittle-are-lcg-cracking-techniques
# https://www.youtube.com/watch?v=EdRK9Ap32Vg
class LCG:
    def __init__(self, nbits):
        self.nbits = nbits
        # finite group (galois field), 2 possible coefficients (0 and 1)
        R = GF(2)['x'] 
        mod = 0
        while True:
            # get random n degree polynomial
            mod = R.random_element(degree=nbits)
            # until it finds an irreducible polynomial
            if mod.is_irreducible():
                break
        assert mod.degree() == nbits
        # modular arithmetic with 2^n elements?
        self.F = GF(2 ** nbits, 'x', modulus=mod)
        # get a and b from F
        self.a = self.F.random_element()
        self.b = self.F.random_element()
        self.m = mod
        # get state from F
        self.state = self.F.random_element()

    def __next__(self):
        # always mult by a, add to b
        self.state *= self.a
        self.state += self.b
        
        # return this state, shifted right by 192*2/3 = 128 bits
        # im left with 64 bits
        return self.state.to_integer() >> ((self.nbits * 2) // 3)


# 192 bits
L = LCG(64 * 3)

# create 200 values
values = [next(L) for _ in range(200)]
print(f'{values = }')

# get v1 and v2 from LCG
v1 = next(L)
v2 = next(L)
# key = v1 + v2 * 2^64
# in binary: first 64 bits are v2, last 64 are v1 (128 bit key)
key = v1 + v2 * pow(2, 64)
key = int.to_bytes(int(key), 16)

flag = 'crew{*** REDACTED ***}'
# use this in AES, with ECB mode (!!)
cipher = AES.new(key, AES.MODE_ECB)

msg = cipher.encrypt(pad(flag.encode(), 16))
print(f'{msg = }')
