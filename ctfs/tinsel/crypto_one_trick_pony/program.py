i=0
big=1000000
while True:
    if i%big==0: print(i)
    i+=1
    i%=(big*big)
