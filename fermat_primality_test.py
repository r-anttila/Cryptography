'''
This module provides a primality test for natural numebers which makes use of Fermat's Little Theorem (FLT).
Notice that it is impossible to use solely FLT to prove the primality of a number so we use a probability based
method and calculate the possible witnesses of n up to n-1. This method is obviously very inefficient but is 
implemented as a simplest possible method.
'''

import math

def flt_test(n):
    '''
    Tests if the number n is prime.

    ------
    Returns:
    ------
    0: if the number n is prime (with high probability).
    (int): The first Fermat witness of n if the number is not prime i.e the number a for which a^n = a (mod n)
    '''

    for i in range (2,n):
        if pow(i,n,n) != i:
            return i

    return 0
