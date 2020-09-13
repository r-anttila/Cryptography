# Cryptography
This repo contains python implementations of multiple cryptographic algorithms.
The source material is listed below but the main source is the book "An Introduction to Mathematical Cryptography" by J. Hoffstein, J. Pipher and J.H. Silverman. 

# Algorithms
## Primality tests
This repository contains implementations of two pure primality checks, that is algorithms which check if the number is composite, but do not provide the prime factorization of the number. The implemented algorithms are

### Fermat Prime Number Test
This algorithm uses the well known result in number theory called [Fermat's Little Theorem](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem), which states that if p is a prime number, then for any natural number a

a^p=a (mod p).

To check if a natural number n is prime, the algorithm checks each number a between 1 and n-1 to see if the equation above is satisfied. If the equation is not satisfied for any of the numbers a, then we know that the number n is composite, but using this method we cannot get a definite proof of the primality of the number.

### Miller-Rabin Primality Test
The second "pure" primality test is the [Miller-Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test). See the link above or section 3.4 in the book by Hoffstein et. al. for details.

## Prime Factorization Algorithms
In addition to primality checks, the repository also contains multiple algorithms which aim to provide the prime factorization of a given number.

### Pollard p-1 algorithm

### Pollard rho algorithm

## Algorithms for Solving the Discrete Logarithm Problem
A number of methods for solving the discrete logarithm problem (DLP) are implemented. The problem in DLP is solving for x in the equation 

g^x=h

in the finite field F_p, where g is a primitive root for F_p. The following algorithms are implemented.

### Shanks Babystep-Giantstep algorithm

### Pohlig-Helman algorithm

# References
1. Hoffstein, J., Piper, J., Silverman, J.H (2008) *An Introduction to Mathematical Cryptography*, Springer Science+Business Media, LLC
2. Leinonen, M. (2020) *801698S-Cryptography Lecture Notes*, University of Oulu, unpublished 