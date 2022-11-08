from math import sqrt
import timeit

# functional approach
def is_primef(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False

    def check_divs(x, d):
        if d*d > x:
            return True
        if x % d == 0:
            return False
        return check_divs(x, d+2)
    return check_divs(x, 3)

# imperative approach
def is_primei(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False

    sq = int(sqrt(x))
    for div in range(3, sq+1, 2):
        if x % div == 0:
            return False
    return True
    
# approach using list comprehension
def is_primels(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False

    sq = int(sqrt(x))
    divs = [1 if x % div == 0 else 0 for div in range(3, sq+1, 2)]
    return sum(divs) == 0

# dodatkowo sito eratostenesa
def sito(n):
    if n < 2:
        return []

    prime = [True for x in range(n+1)]
    prime[0] = prime[1] = False

    for i, b in enumerate(prime):
        if i*i >= n:
            break
        if b:
            for xi in range(i*i, n+1, i):
                prime[xi] = False
    
    return [x for x in range(n+1) if prime[x]]



def pierwsze_funkcyjna(n):
    return list(filter(is_primef, range(2, n+1)))

def pierwsze_imperatywna(n):
    res = []
    for x in range(2, n+1):
        if is_primei(x):
            res.append(x)
    return res

def pierwsze_skladana(n):
    return [x for x in range(2, n+1) if is_primels(x)]

def test_imp(n):
    start_time = timeit.default_timer()
    res = pierwsze_imperatywna(n)
    end_time = timeit.default_timer() 
    return (end_time-start_time, res)

def test_skl(n):
    start_time = timeit.default_timer()
    res = pierwsze_skladana(n)
    end_time = timeit.default_timer() 
    return (end_time-start_time, res)

def test_funkc(n):
    start_time = timeit.default_timer()
    res = pierwsze_funkcyjna(n)
    end_time = timeit.default_timer() 
    return (end_time-start_time, res)

def test_sito(n):
    start_time = timeit.default_timer()
    res = sito(n)
    end_time = timeit.default_timer() 
    return (end_time-start_time, res)

def compare(ns):

    top = ['imperatywna', 'funkcyjna', 'skladana', 'sito erastotenesa']

    shft = len(str(max(ns)))
    print('n', end = ' '*shft)
    print(' '.join(map(lambda x : x.ljust(2), top)))

    for n in ns:
        timers = [test_imp(n)[0], test_skl(n)[0], test_funkc(n)[0], test_sito(n)[0]]
        print(n, f'{timers[0]:.2e}'.rjust(11-len(str(n))+shft),  f'{timers[1]:.2e}'.rjust(9), f'{timers[2]:.2e}'.rjust(3), f'{timers[3]:.2e}'.rjust(5))

if __name__ == "__main__":
    compare([10**x for x in range(1, 6)])