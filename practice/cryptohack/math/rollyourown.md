roll your own: writeup
===

# intro

we get a system with variable $q$, a known 512 bit prime

we are solicited $g \geq 2$ and $n \geq 2$, such that

$g^q \equiv 1 \mod n$, where

once we find it, we'll get

$g^x \mod n$, for a random $x$ between 0 and $q$. if we manage to find $x$, we'll get the flag

# pre-sol

there's an initial $x$ but it doesn't seem to be used. the `check_params` test seems to follow a test to see if the $(g,n)$ tuple makes a field of order $q$ or a multiple of it. choosing $n = q$ makes the order $q-1$ instead. what actually needs to be done here is find $n$ s.t. $\phi(n)$ has q as a factor. numbers $kq + 1$ for some integer $k$ can work. 

https://en.wikipedia.org/wiki/Carmichael_number i also thought of a solution supplying these numbers. they can for example trick the Fermat primality test.

both of these approaches didn't seem to possibly ease the discrete log problem though. but they might come in handy for other challenges

# sol

turns out that if we choose $n = q^2$ and $g = 1+q$, we can see that

$$g^x \equiv (1+q)^x \equiv 1^x + \binom{x}{1} 1^{x-1} q + \binom{x}{2} 1^{x-2} q^2 + \cdots + q^x \mod q^2$$

$$\equiv 1 + xq \mod q^2$$

lets call this number $h$. normally we could do $x \equiv (h-1) q^{-1} \mod q^2$, but clearly $gcd(q, q^2) \ne 1$, so there's no inverse.

but notice that since $x$ is between 0 and $q$, $1+xq$ will only surpass $q^2$ when $x = q$ which is negligible. so we can find $x$ as $\frac{h-1}{q}$ (integer division)