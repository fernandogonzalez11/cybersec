quantum safe
===

$$\vec c = A \cdot \vec m + \vec e$$

where $A$ is a defined matrix, $\vec e$ is a random error vector (short with respect to $A$ and $\vec m$, $\vec m$ is (`ord(c)`, random, random)

we can rewrite this ciphertext equation

$$\vec c - A \cdot \vec m = \vec e$$

we can now see whats the "path" to find, for example, $e_1$

$e_1 = c_1 - (m_1 \cdot A_{11} + m_2 \cdot A_{12} + m_3 \cdot A_{13})$

we can replicate this behavior for all elements of $\vec e$:

$$\begin{align*}
1 \cdot (c_1, c_2, c_3) + \\
m_1 \cdot (-A_{11}, -A_{21}, -A_{31}) + \\
m_2 \cdot (-A_{12}, -A_{22}, -A_{32}) + \\
m_3 \cdot (-A_{13}, -A_{23}, -A_{33}) = \\
(c_1, c_2, c_3)
\end{align*}$$

this is already a lattice, but let's put more columns to get $m_1$:

$$\begin{align*}
1 \cdot (c_1, c_2, c_3, 0) + \\
m_1 \cdot (-A_{11}, -A_{21}, -A_{31}, 1) + \\
m_2 \cdot (-A_{12}, -A_{22}, -A_{32}, 0) + \\
m_3 \cdot (-A_{13}, -A_{23}, -A_{33}, 0) = \\
(c_1, c_2, c_3, m_1)
\end{align*}$$

this didn't work but it could've been a good idea. maybe i could make it work by using various equations so that the lattice is bigger, or some rescaling issue.

# actual sol

turns out $\vec r$ is fixed, so for 2 ciphertexts:

$$\begin{align*}
\vec c_1 = A \cdot m_1 + \vec r \\
\vec c_2 = A \cdot m_2 + \vec r
\end{align*}$$

so their difference is $\vec c_1 - \vec c_2 = A \cdot (\vec m_1 - \vec m_2)$. this means $\vec m_1 - \vec m_2 = A^{-1} \cdot (\vec c_1 - \vec c_2)$

so we can gather the difference between one character and the next, for all characters. so we can bruteforce the first character (or not, we know it's `H` due to the flag format), and increment or decrement according to the first value of the difference. this yields

`HTB{r3duc1nG_tH3_l4tTicE_l1kE_n0b0dY's_pr0bl3M}`

ok my bad bro....