p = 28151

for x in range(2, p):
    a_cycle = False
    for i in range(2, p):
        if pow(x, i, p) == x:
            a_cycle = True
            break

    if not a_cycle:
        print(x, "found")
        break

    print(x, "didn't work")



"""
from primefac import primefac

p = 28151
totient = p - 1 
totient_factors = set(primefac(totient))

for candidate in range(2,p):
    is_primitive = True

    for factor in totient_factors:
        exp = totient//factor
        power = pow(candidate,exp,p)
        print(f'Candidate: {candidate}, factor: {factor} , result: {power}')

        if power == 1:
            is_primitive = is_primitive and False
            break
        else:
            is_primitive = is_primitive and True
    
    if is_primitive:
        print(f'\nPrimitive Found:\n{candidate} is the smallest primitive for p={p}\na^((p-1)/q) != 1 mod p for each prime q : q|(p-1)')
        break
"""