
import math
import numpy as np
import sieves

def pe58():
    i = 1
    ll= [3,5,7,9]
    lp = [2,3,5,7]
    num = 3
    den = 5
    ratio = num / den
    while True:

        ll = [ll[0] + 2+ 8*i, ll[1] + 4+ 8*i, ll[2]+ 6+8*i, ll[3]+ 8+8*i]

        sr = int(math.sqrt(ll[3]))
        subll = sieves.sieve_partial(sr, lp)
        lp += subll

        num += len([i for i in ll if not sieves.has_prime_factor(i, lp)])
        den += 4

        print('i is: ' + str(i) + '. ratio is: ' + str(num/den))
        if (num/den) < 0.1:
            break
        i += 1
    print('solution is: ' + str(2 * i +3))

    return None

if __name__ == '__main__':
   pe58()