# GCD

```
gcd(a, b) = gcd(b, a mod b)
gcd(a, 0) = a
```

# Extended GCD

Find $x, y$ such that $xa + yb = g$, where $g$ is the GCD (by Bézout's identity this always exists)

```
x1, y1 = gcd(b, a mod b)
x = y1
y = x1 - y1 * floor(a/b)
```

```py
def egcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1

    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return (x0, y0)

def gcd(a, b):
    x, y = egcd(a, b)
    return x*a + y*b

def lcm(a, b):
    return (a*b) // gcd(a, b)
```