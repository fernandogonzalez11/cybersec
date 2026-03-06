quantum safe: writeup (lattice ver)
===

we're given a bunch of ciphertexts defined as 

$$\vec c_i = \vec m_i \cdot A + \vec r$$

where $\vec m = (x, y, z)$ where:

* $x = ord(flag_i)$
* $y, z \in \{0..100\}$

and $\vec r$ is all numbers $\in {0..10}$. it's really important to note that $\vec r$ is fixed for all ciphertexts

from here we can see that

$$\vec c = (x,y,z) \cdot A + \vec r$$

$$\vec c = x \vec A_1 + y \vec A_2 + z \vec A_3 + \vec r$$

we could aim to find all $(x,y,z)$ independently, or better yet, find $\vec r$. if we find $\vec r$, we can do

$$(\vec c_i - \vec r) \cdot A^{-1} = \vec m_i$$

now, we know that the flag must start with `HTB{`. so, in our case,

$$\vec c - x \vec A_1 = y \vec A_2 + z \vec A_3 + \vec r$$

we can dissect this equation as:

1. $\vec c - x \vec A_1$: known
2. $y \vec A_2 + z \vec A_3$: vectors known, coefs unknown
3. $\vec r$: unknown

it's interesting because since we know the vectors in (2), we can make a lattice $\mathcal{L} = \{\vec A_2,  \vec A_3\}$, and see that $y \vec A_2 + z \vec A_3$ is in that lattice

so, **since $\vec r$ is small** we could solve CVP to find the closest vector to $\vec c - x \vec A_1$, which should be $y \vec A_2 + z \vec A_3$. so we just do:

$$(\vec c - x \vec A_1) - (y \vec A_2 + z \vec A_3) = \vec r$$

# conclusions

* I misnomered $\vec m \cdot A$ with $A \cdot \vec m$, thinking $\vec m$ and $\vec r$ could be thought as vertical vectors, which tripped me up a lot. I should be more careful about left vs right matrix multiplication
* This exercise shows a very nice way to see what is a CVP versus an SVP one!