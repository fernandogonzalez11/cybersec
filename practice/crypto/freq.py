def analyze(s: str):
    freqs = [[0, chr(i)] for i in range(ord('A'), ord('Z')+1)]

    chars = 0

    for l in range(ord('A'), ord('Z')+1):
        for c in s:
            if c == chr(l):
                freqs[l - ord('A')][0] += 1
                chars += 1    

    return freqs, chars


if __name__ == "__main__":
    with open('input.txt') as f:
        s = f.read()

    freqs, chars = analyze(s)
    freqs.sort(reverse=True)
    for f in freqs:
        perc = f[0] / chars * 100
        print(f"{f[1]}: {f[0]}, {perc:.2f}")

    s = s
    print(s)
