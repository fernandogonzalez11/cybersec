# legendre symbol

$(\frac{a}{p}) = a^{\frac{p-1}{2}} \mod p$

1 if a is quadratic residue

-1 if it's not

0 only if it's 0

## properties

---

if $p \equiv 3 \mod 4$ and $(\frac{a}{p}) = 1$,

$x^{\frac{p+1}{4}} \equiv \sqrt{x} \mod p$

general algorithm to get sqrt: Tonelli-Shanks

---

$(\frac{ab}{p}) = (\frac{a}{p})(\frac{b}{p})$

$(\frac{-1}{p})$ :

* 1 if p is 1 mod 4
* -1 if p is -1 mod 3


can be considered a PRF: https://legendreprf.dankrad.vercel.app/