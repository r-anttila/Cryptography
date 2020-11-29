'''
This module provides a primality test for natural numebers which makes use of the Miller-Rabin algorithm.
'''
import math

first_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def miller_rabin_test(n):
    '''
    Tests if the number n is prime.

    ------
    Returns:
    ------
    True: If n is prime
    False: otherwise
    '''
    if n in first_primes:
        return True

    n2 = n-1
    k = 0
    q = 0
    not_witness_num = 0

    # Computing the numbers k, q for which n-1=2^k*q
    while True:
        if n2 % 2 == 0:
            n2 = n2//2
            k += 1
        else:
            q = n2
            break

    # The Miller-Rabin test
    for a in range(2, math.ceil(math.log2(n) ^ 2)):
        not_witness = False
        if math.gcd(a, n) != 1:
            continue
        cur = pow(a, q, n)
        if cur == 1 or cur == n-1:
            not_witness = True
            continue
        for _ in range(k):
            cur = pow(cur, 2, n)
            print(cur)
            if cur == n-1:
                not_witness = True
                break
        if not_witness:
            continue

        return False

    return True


if __name__ == "__main__":
    print(miller_rabin_test(2000002))
