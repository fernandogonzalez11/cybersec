import hashlib, json
from Crypto.Util.number import getPrime, isPrime
from random import randint

FLAG = open("flag.txt").read()

print(FLAG.strip("HTB{}"))

assert len(FLAG.strip("HTB{}")) == 79 # interesting..... len(FLAG) = 82

# https://pcwww.liv.ac.uk/~karpenk/JournalUDT/vol18/no1/06_GyMu_pdf.pdf
# https://en.wikipedia.org/wiki/Quadratic_residuosity_problem
class TinselRNG:
    def __init__(self, bits):
        self.prime = getPrime(bits) # 34 bit prime
        self.seed = randint(1, self.prime)
        # self.prime = 14529203489
        # self.seed = 12345

    def sparkle_bit(self):
        if self.seed == 0:
            self.seed += 1
        while True:
            # legendre symbol?
            legendre = pow(self.seed, (self.prime-1)//2, self.prime)
            yield int(legendre == 1)
            self.seed = (self.seed + 1) % self.prime
            # we skip 0, the only num which gives legendre 0
            if self.seed == 0:
                self.seed += 1

    # generate l sparkles
    def gather_sparkles(self, l):
        bits = ''
        for i, b in enumerate(self.sparkle_bit()):
            if i == l: break
            bits += str(b)
        return int(bits, 2)

assert isPrime(PRIME := 0x1a66804d885939d7acf3a4b413c9a24547b876e706913adec9684cc4a63ab0dfd2e0fd79f683de06ad17774815dfc8375370eb3d0fb5dce0019bd0632e7663a41) # 259 bit prime

def frostscribe_signature(msg):
    # important note: the HASH is what's used for etch!
    hash = hashlib.sha512(msg.encode()).digest()
    hash_int = int.from_bytes(hash, "big") % PRIME

    print(f'{hash_int = }') # 509

    exp = frostrng.gather_sparkles(500)
    print(f'{exp = }')

    etch = pow(hash_int, exp, PRIME)
    return {"signature": str(etch)}

frostrng = TinselRNG(34)

print(f'{frostrng.prime = }')
# print(f'{frostrng.seed = }')

LIMIT = 2_000

print("Welcome to the Snowglobe Cipher Booth!\n")
while True:
    if LIMIT <= 0:
        print("The lantern dims for today...")
        break

    print("1) Etch Message Rune")
    print("2) Request Wrapped Starshard")
    print("3) Leave Booth")

    choice = input("> ").strip()

    if choice == "1":
        msg = input("Whisper your message: ")
        print(json.dumps(frostscribe_signature(msg)))
        LIMIT -= 1

    elif choice == "2":
        print(len(FLAG)*8)
        snow_otp = frostrng.gather_sparkles(len(FLAG)*8) # 664
        user_otp = int(input("Reveal my snow-otp (in bits): "), 2)
        if user_otp == snow_otp:
            print(json.dumps({"starshard": FLAG}))
        else:
            print(json.dumps({"starshard": "HTB{fake_flag_for_testing}"}))
        break

    elif choice == "3":
        print('May your lantern stay warm. Farewell...')
        break

    else:
        print("That choice jingled wrong.")
