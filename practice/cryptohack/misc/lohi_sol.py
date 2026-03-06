from pwn import *
from json import dumps, loads

mod = 2**61 - 1  # 9th mersenne prime
VALUES = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
          'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
SUITS = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

# card# = suit * len(VALUES) + val

print([suit+value for suit in SUITS for value in VALUES])

BASE = 52

def calc_params(seq: list):
    a = ((seq[1]-seq[2]) * pow(seq[0]-seq[1], -1, mod)) % mod
    b = (seq[1]-a*seq[0]) % mod

    return (a, b)

conn = remote("socket.cryptohack.org", 13383)

def recv_json():
    print(json := loads(conn.recvline().decode()))
    return json

def send_json(json):
    conn.sendline(dumps(json).encode())

def get_val(hand: str):
    extracted = hand.split(" of ")
    val = VALUES.index(extracted[0])
    suit = SUITS.index(extracted[1])
    return suit * len(VALUES) + val

def get_roundnum(msg: str):
    return int(msg.split("after ")[1].split(" ")[0])

round_strs = []
cur = []
pending_new = False
first = True
while len(round_strs) < 3:
    j = recv_json()
    if "error" in j:
        exit()

    # this hand still belongs to the old shuffle
    cur.append(get_val(j["hand"]))

    if "reshuffle the deck" in j["msg"] and not first:
        round_strs.append(cur)
        cur = []          # next hand starts new shuffle
    
    first = False   

    send_json({"choice": "lower"})

round_strs.append(cur)

seq = []
for i in range(3):
    round_strs[i].reverse()
    n = 0
    for b in range(len(round_strs[i])):
        n += round_strs[i][b] * pow(BASE,b)

    seq.append(n)

print(seq)

a, b = calc_params(seq)
assert (a*seq[1]+b) % mod == seq[2]


def rebase(n, b=52):
    if n < b:
        return [n]
    else:
        return [n % b] + rebase(n//b, b)

prev = None

while True:
    seq.append((a*seq[-1]+b) % mod)
    deals = rebase(seq[-1], BASE)
    deals.reverse()

    for d in deals:
        cur = d % len(VALUES)

        if prev is not None:
            if cur < prev:
                send_json({"choice": "lower"})
            else:
                send_json({"choice": "higher"})
            recv_json()

        prev = cur
