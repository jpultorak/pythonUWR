from zad1 import is_primef, is_primei, is_primels, sito
import timeit
# Generating perfect numbers using Euclid-Euler theorem (https://en.wikipedia.org/wiki/Euclid%E2%80%93Euler_theorem) 
# naive sqrt(N) implementations -> generates perfect numbers up to 2658455991569831744654692615953842176
# with better test like Miller Rabin we could probably do much better

# pre generating primes
# for larger values functional/comprehension approach might not work
max_prime = 100
primes = sito(max_prime)


def doskonale_imperatywna(n):
    res = []
    for p in primes:
        x = 2**p-1
        if(2**(p-1)*x > n):
            break
        if is_primei(x):
            res.append(2**(p-1)*x)
    return res

# looks through entire prime lists, so will be much slower than imperative
def doskonale_skladana(n):
    res = [2**(p-1)*(2**p-1) for p in primes if 2**(p-1)*(2**p-1) <= n and is_primels(2**p-1)]
    return res

# due to recursion in is_primef, max depth recursion will be reached very quickly
# so used imperative implementation for prime checking 

# not very functional, but without it very very slow
# normal filter function was looking through whole prime lists
# now we break out of loop if we find first prime bigger than we want
def filter_sorted(xs, n):
    res = []
    for x in xs:
        if x > n:
            break
        res.append(x)
    return res

def doskonale_funkcyjna(n):
    res = filter(lambda p: is_primei(2**p-1), primes)
    res = map(lambda p: 2**(p-1)*(2**p-1), res)
    res = filter_sorted(res, n)
    return res

def test_imp(n):
    start_time = timeit.default_timer()
    res = doskonale_imperatywna(n)
    end_time = timeit.default_timer() 
    return (end_time-start_time, res)

def test_skl(n):
    start_time = timeit.default_timer()
    res = doskonale_skladana(n)
    end_time = timeit.default_timer() 
    return (end_time-start_time, res)

def test_funkc(n):
    start_time = timeit.default_timer()
    res = doskonale_funkcyjna(n)
    end_time = timeit.default_timer() 
    return (end_time-start_time, res)

def compare(ns):

    top = ['imperatywna', 'funkcyjna', 'skladana']

    shft = len(str(max(ns)))
    print('n', end = ' '*shft)
    print(' '.join(map(lambda x : x.ljust(2), top)))

    for n in ns:
        timers = [test_imp(n)[0], test_skl(n)[0], test_funkc(n)[0]]
        print(n, f'{timers[0]:.2e}'.rjust(11-len(str(n))+shft),  f'{timers[1]:.2e}'.rjust(9), f'{timers[2]:.2e}'.rjust(3))
    
if __name__ == '__main__':

    compare([10**(2*x) for x in range(2, 10)])

    # slow
    print(doskonale_skladana(100000000000000000000000000000000))
    
    # fast
    print(doskonale_imperatywna(100000000000000000000000000000000))

    # very slow
    print(doskonale_funkcyjna(100000000000000000000000000000000))

    # conclusion: imperative is clear winner in this one, due to break statement

    # will take 30-60s
    #print(doskonale_imperatywna(2658455991569831744654692615953842176))