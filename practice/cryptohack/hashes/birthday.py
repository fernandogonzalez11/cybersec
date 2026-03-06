# https://data140.org/textbook/content/chapter-01/birthday-problem/

import numpy as np

bits = 11
N = 1<<bits

print(N)

def p_collision(n):
    individuals_array = np.arange(n)
    return 1 - np.prod( (N - individuals_array)/N )

p = 0.75

def ok(n):
    return p_collision(n) >= p

l = 1
r = 2
while not ok(r): r *= 2

print(r)

while (r-l>1):
    m = (r-l)//2+l
    if ok(m): r = m
    else: l = m

print(r, p_collision(r))

