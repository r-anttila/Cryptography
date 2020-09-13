'''
This module provides a prime factorization algorithm called the Pollard p-1 algortihm.
'''
import math

def pollard_for_a(n,a,b):
    '''
    The Pollard p-1 algorithm to factorize n. This function tries the factorization using number
    a up to exponent b!.

    --------
    Returns:
    --------
    0: if no factor was found.
    int: the prime factor of n found by the algorithm.
    '''
    for j in range(2,b+1):
        a = pow(a,j,n)
        d = math.gcd(a-1,n)
        if 1<d<n:
            return d
    return 0
