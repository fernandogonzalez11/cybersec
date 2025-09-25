def analyze(s: str):
    freqs = [[0, chr(i)] for i in range(ord('A'), ord('Z')+1)]

    chars = 0

    for l in range(ord('A'), ord('Z')+1):
        for c in s:
            if c == chr(l):
                freqs[l - ord('A')][0] += 1
                chars += 1    

    return freqs, chars

the_freqs = [0 for i in range(26)]

if __name__ == "__main__":
    with open('input.txt') as f:
        s = f.read()

    freqs, chars = analyze(s)
    freqs.sort(reverse=True)
    for f in freqs:
        perc = f[0] / chars * 100
        print(f"{f[1]}: {f[0]}, {perc:.2f}")

    for f in freqs: print(f[1],end='')
    print()

    s = s \
        .replace('S', 'e') \
        .replace('Q', 't') \
    
    print(s)
    
    for i in range(len(s)):
        c = s[i]
        if (c >= "A" and c <= "Z"):
            if not (i < len(s)-1 and s[i-1] == 't' and s[i+1] == 'e'):
                print("-", end='')
            else:
                the_freqs[ord(c)-ord('A')] += 1
                print(c, end='')
        else: print(c, end='')

print(the_freqs)