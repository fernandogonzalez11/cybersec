# modular inverses

find $a^{-1} \mod N$, such that $a a^{-1} \equiv 1 \mod N$

## with egcd

when `gcd(a, N) = 1`,

$xa + yN = 1$

$xa = 1-yN$

$xa \equiv 1 \mod N$

$x \equiv a^{-1} \mod N$

so just find `X, Y := egcd(a, N)`, then `X` is the inverse

## with binexpmod

when `gcd(a, N) = 1`,

$a^{\phi(N)} \equiv 1 \mod N$

so $a^{-1} \equiv a^{\phi(N)-1} \mod N$

$N = p$ prime => $\phi(p) = p-1$

$N = pq$ => $\phi(pq) = (p-1)(q-1)$