# https://github.com/LeonardoE95/yt-en/blob/main/src/2024-02-07-pseudo-randomness-breaking-lcg/content/code/attack-lcg.py

#!/usr/bin/env python3
#
# Code that shows how to attack a simple LCG PRNG by obtaining a
# series of direct outputs from the PRNG.
#
# Refs:
# - https://security.stackexchange.com/questions/4268/cracking-a-linear-congruential-generator
#
import random
import sys
import math
from functools import reduce
# from lcg import LCG

# -------------------------------------

def compute_modulus(outputs):
    ts = []
    for i in range(0, len(outputs) - 1):
        ts.append(outputs[i+1] - outputs[i])
        
    us = []
    for i in range(0, len(ts)-2):
        us.append(abs(ts[i+2]*ts[i] - ts[i+1]**2))

    modulus =  reduce(math.gcd, us) #!
    return modulus

def compute_multiplier(outputs, modulus):
    term_1 = outputs[1] - outputs[2]
    term_2 = pow(outputs[0] - outputs[1], -1, modulus) #!
    a = (term_1 * term_2) % modulus
    return a

def compute_increment(outputs, modulus, a):
    b = (outputs[1] - outputs[0] * a) % modulus
    return b

# -------------------------------------    

# 
# Implementation of a basic Linear Congruential Generator, one of the
# simplests form of Pseudo-Random Number Generator.
#
# Notice that a basic LCG is not cryptographically safe, meaning that
# a malicious attacker, by observing consecutive outputs from the
# generator, is able to infer the internal state of the generator and
# thus also the next numbers the generator will produce.
#
# For this reason, you should not use this generator in security
# contexts where predictability might imply dangerous consequences.
# 
class LCG(object):
    def __init__(self, seed=1337, a=1103515245,b=12345,c=2147483648):   
        self.x = seed
        self.a = a
        self.b = b
        self.c = c

    def next(self):
        self.x = (self.x * self.a + self.b) % self.c
        return self.x

def main():
    # prng = LCG(seed=1337, a=1337, b=42, c=444447)
    outputs = [14841917648858837769, 9575471537143015742, 15844238770919434615, 5212260032608174747]
    
    c = compute_modulus(outputs)
    a = compute_multiplier(outputs, c)
    b = compute_increment(outputs, c, a)

    print(f"c={c}")    
    print(f"a={a}")
    print(f"b={b}")
    
    l = LCG(seed=7564345426168321381, a=10015413974664223849678453908501686134, b=8367217595136670028056425990839022488, c=16695300454955771140924638859284922307)
    print(l.next())
    
if __name__ == "__main__":
    main()
