
import numtheory
from math import sqrt


def sieve(n):
    """
    Implements a version of the Sieve of Eratosthenes
    :param n: a positive integer
    :return: a list of all primes <= n
    """

    if n <=1:
        ans = []
    else:
        ans = [2]

        for i in range(2,n+1):
            rem = 1
            isr = int(sqrt(i))
            for j in range(len(ans)):
                rem = i % ans[j]

                if (rem == 0) or (j > isr):
                    break

            if (rem > 0):
                ans.append(i)
    return ans


def sieve2(n):
    """
    Implements a version of the Sieve of Eratosthenes
    :param n: a positive integer
    :return: a list of all primes <= n
    """

    if n <= 1:
        ans = []
    else:
        ans = [2]

        for i in range(2, n + 1):
            rem = 1

            for j in range(len(ans)):
                rem = i % ans[j]

                if (rem == 0) or (j*j > i):
                    break

            if (rem > 0):
                ans.append(i)
    return ans

def sieve_partial(n, lp):
    """
    Implements a version of the Sieve of Eratosthenes
    :param n: a positive integer
    :param lp: the list of the first len(p) primes
    :return: a list of all primes <= n
    """

    if n <= 1:
        ans = []
    else:
        ans = []
        lp = lp.copy()
        #ans = sorted(p for p in lp if p <= n)
        ml = max(lp)
        for i in range(ml + 1, n + 1):
            rem = 1

            for j in range(len(lp)):

                rem = i % lp[j]

                if (rem == 0) or (j*j > i):
                    break

            if (rem > 0):
                ans.append(i)
                lp.append(i)
    return ans


sieve_partial(11,[2,3,5, 7])

def has_prime_factor(n, lp):
    """
    Checks whether n is divided by at least one of the prime numbers in list lp
    :param n: a positive integer
    :param lp: a list of primes
    :return: True if at least one element of the list lp is a factor of n
    """
    if lp ==[]:
        ans = False
    else:
        rn = int(sqrt(n))
        lt = [e for e in lp if e <= rn or e == n]
        rem = 1
        for e in lt:
            rem = max(n,e)%min(n,e)
            if rem == 0:
                break
        ans = rem == 0
    return ans


def is_prime(n):
    """

    :param n: a positive integer
    :return: True if n is a prime number
    """
    if n <= 1:
        ans = True
    else:
        lp = sieve(min(n-1, int(sqrt(n))+1))
        ans = has_prime_factor(n, lp)
    return not ans


def is_coprime(n, l):
    """

    :param n: a positive integer
    :param l: a list of positive integers
    :return: True if n is a coprime w.r.t. all elements of list l
    """
    if l ==[]:
        ans = True
    else:
        rem = 2
        for e in l:
            rem = numtheory.gcd(n,e)
            if rem == 1:
                break
        ans = rem == 1
    return ans


def factor_decomp(n):
    """

    :param n: a positive integer
    :return: list of prime numbers that divide n
    """
    lp = sieve(int(sqrt(n)))
    ans = [p for p in lp if n%p == 0]
    return ans


def factor_decomp2(n):
    """

    :param n: positive integer
    :return: list of tuples of integers in the form (p,e) where e>0 and e is the maximal
    value such that p**e divides n
    """
    lp = factor_decomp(n)
    ans = []
    m = n
    for p in lp:
        e = 0
        rem = 0
        while True:
            rem = m % p
            if rem > 0:
                break
            m = m / p
            e += 1
        ans.append((p,e))
    return ans


def factor_decomp3(n):
    """

    :param n: positive integer
    :return: list of tuples of integers in the form (p,e) where e>0 and e is the maximal
    value such that p**e divides n
    """
    lp = sieve(int(sqrt(n)))
    ans = []
    m = n
    for p in lp:
        e = 0
        rem = 0
        while True:
            rem = m % p
            if rem > 0:
                break
            m = m / p
            e += 1
        if e >0:
            ans.append((p,e))
    return ans

