
import timeit
import sieves

def tests():
    timer  = timeit.Timer(stmt = 'factor_decomp2(1108809)', setup = 'from sieves import factor_decomp2')
    result = timer.repeat(repeat=1000, number = 1000)
    print(len(result))
    print(sum(result))


    timer2  = timeit.Timer(stmt = 'factor_decomp3(1108809)', setup = 'from sieves import factor_decomp3')
    result2 = timer2.repeat(repeat=1000, number = 1000)
    print(len(result2))
    print(sum(result2))

#tests()


def tests_sieve():
    timer  = timeit.Timer(stmt = 'sieve_partial(100,[2, 3, 5, 7, 9, 11, 13, 17, 19, 23, 29])', setup = 'from sieves import sieve_partial')
    result = timer.repeat(repeat=1000, number = 10)
    print(len(result))
    print(sum(result))


    timer2  = timeit.Timer(stmt = 'sieve2(100)', setup = 'from sieves import sieve2')
    result2 = timer2.repeat(repeat=1000, number = 10)
    print(len(result2))
    print(sum(result2))

tests_sieve()



