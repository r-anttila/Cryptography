'''
This module provides a primality test for natural numebers which makes use of the Miller-Rabin algorithm.
'''

def miller_rabin_test(n):
    '''
    Tests if the number n is prime.

    ------
    Returns:
    ------
    0: if the number n is prime (with high probability). 
    (int): The first Miller-Rabin witness of n if the number is not prime i.e. the first number which does 
    not satisfy the Miller-Rabin conditions.
    '''
    import math

    n2 = n-1
    k = 0
    q = 0
    not_witness_num=0

    # Computing the numbers k, q for which n-1=2^k*q
    while True:
        if n2 % 2 == 0:
            n2=n2//2
            k += 1
        else:
            q = n2
            break
        
    #The Miller-Rabin test
    for a in range (2, n):
        not_witness = False
        if math.gcd(a,n) != 1:
            continue
        cur = pow(a,q,n)
        if cur == 1 or cur == n-1:
            not_witness_num += 1
            continue
        for _ in range(k):
            cur = pow(cur, 2, n)
            if cur == n-1:
                not_witness_num += 1
                not_witness = True
                break
        if not_witness:
            continue
        #Use that >=75% of numbers between 1 and n-1 are witnesses for composite number
        elif n-1-not_witness_num/(n-1)>=0.75:
            return 0
        
        return a
        

    return 0



            
print(miller_rabin_test(2000003))