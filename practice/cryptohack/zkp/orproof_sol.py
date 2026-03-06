from pwn import *
from json import dumps, loads
from Crypto.Util.number import long_to_bytes, bytes_to_long
from hashlib import sha512
from params import p, q, g


# w,y for the relation `g^w = y mod p` we want to prove knowledge of
# w = random.randint(0,q)
# y = pow(g,w,p)
w0 = 0x5a0f15a6a725003c3f65238d5f8ae4641f6bf07ebf349705b7f1feda2c2b051475e33f6747f4c8dc13cd63b9dd9f0d0dd87e27307ef262ba68d21a238be00e83
y0 = 0x514c8f56336411e75d5fa8c5d30efccb825ada9f5bf3f6eb64b5045bacf6b8969690077c84bea95aab74c24131f900f83adf2bfe59b80c5a0d77e8a9601454e5
# w1 = REDACTED
y1 = 0x1ccda066cd9d99e0b3569699854db7c5cf8d0e0083c4af57d71bf520ea0386d67c4b8442476df42964e5ed627466db3da532f65a8ce8328ede1dd7b35b82ed617
assert (y0%p) >= 1 and (y1%p) >= 1
assert pow(y0, q, p) == 1 and pow(y1, q, p) == 1

conn = remote("archive.cryptohack.org", 11840)
# conn = process(["python3", "./zkp/orproof_chall.py"])


def send_int(x):
    conn.sendline(str(x).encode())

def simulator(y, e):
    z = randint(1, q-1)
    a = pow(g,z,p) * pow(y,-e,p) % p

    return (a, e, z)

def correctness():
    print(conn.recvline())
    print(conn.recvline()) 

    e1 = randint(0, q)
    a1, e1, z1 = simulator(y1, e1)

    r0 = randint(0, q)
    a0 = pow(g, r0, p)

    send_int(a0)
    send_int(a1)

    print(info := conn.recvline())
    s = int(info[25:-1])

    e0 = e1 ^ s
    z0 = r0 + e0*w0

    send_int(e0)
    send_int(e1)
    send_int(z0)
    send_int(z1)        

def specialSoundness():
    print(conn.recvline())

    print(info := conn.recvline())
    y0 = int(info[5:])

    print(y0)

    print(info := conn.recvline())
    y1 = int(info[5:])

    print(conn.recvline())
    print(conn.recvline())

    print(info := conn.recvline())
    a0 = int(info[5:])

    print(info := conn.recvline())
    a1 = int(info[5:])

    print(info := conn.recvline())
    s = int(info[4:])

    print(info := conn.recvline())
    e0 = int(info[5:])

    print(info := conn.recvline())
    e1 = int(info[5:])

    print(info := conn.recvline())
    z0 = int(info[5:])

    print(info := conn.recvline())
    z1 = int(info[5:])

    print(conn.recvline())

    print(info := conn.recvline())
    a0 = int(info[5:])

    print(info := conn.recvline())
    a1 = int(info[5:])

    print(info := conn.recvline())
    s2 = int(info[5:])

    print(info := conn.recvline())
    e02 = int(info[6:])

    print(info := conn.recvline())
    e12 = int(info[6:])

    print(info := conn.recvline())
    z02 = int(info[6:])

    print(info := conn.recvline())
    z12 = int(info[5:])

    
    if e0 - e02 != 0: 
        w = (z0 - z02) * pow(e0 - e02, -1, q) % q
    else:
        w = (z1 - z12) * pow(e1 - e12 % q, -1, q) % q

    send_int(w)

    print(conn.recvline())

def SHVZK():
    print(conn.recvline())

    print(info := conn.recvline())
    y0 = int(info[5:])

    print(info := conn.recvline())
    y1 = int(info[5:])

    print(info := conn.recvline())
    s = int(info[38:])

    # honest cipher bit
    b = randint(0,1)

    if b: y0,y1 = y1,y0

    e1 = random.randint(0,2**511-1)
    a1, e1, z1 = simulator(y1, e1)

    e0 = e1 ^ s
    a0, e0, z0 = simulator(y0, e0)

    if b: a0,e0,z0,a1,e1,z1 = a1,e1,z1,a0,e0,z0

    send_int(a0)
    send_int(a1)
    send_int(e0)
    send_int(e1)
    send_int(z0)
    send_int(z1)

    
correctness()
specialSoundness()
SHVZK()

print(conn.recvline())
print(conn.recvline())