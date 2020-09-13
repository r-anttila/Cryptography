# Cryptography
This repo contains python implementations of multiple cryptographic algorithms.
The source material is listed below but the main source is the book "An Introduction to Mathematical Cryptography" by J. Hoffstein, J. Pipher and J.H. Silverman. 

# Algorithms
## Primality tests
This repository contains implementations of two pure primality checks, that is algorithms which check if the number is composite, but do not provide the prime factorization of the number. The implemented algorithms are

### Fermat Prime Number Test

### Miller-Rabin Primality Test

## Prime Factorization Algorithms
In addition to primality checks, the repository also contains multiple algorithms which aim to provide the prime factorization of a given number.

### Pollard p-1 algorithm

### Pollard rho algorithm

## Algorithms for Solving the Discrete Logarithm Problem
A number of methods for solving the discrete logarithm problem (DLP) are implemented. The problem in DLP is solving for x in the equation 

g^x=h

in the field F_p, where g is a primitive root for F_p. The following algorithms are implemented.

### Shanks Babystep-Giantstep algorithm

### Pohlig-Helman algorithm

# References
1. Hoffstein, J., Piper, J., Silverman, J.H (2008) *An Introduction to Mathematical Cryptography*, Springer Science+Business Media, LLC
2. Leinonen, M. (2020) *801698S-Cryptography Lecture Notes*, University of Oulu, unpublished 