from itertools import product
from tableprint import tabliczka
import sys

def sudan(n, x, y):
    if n == 0:
        return x+y
    if y == 0:
        return x
    
    return sudan(n-1, sudan(n, x, y-1), sudan(n, x, y-1) + y)

# ugly, should have used decorator
# worst case time coplexity - O(n*x*y)
memo = {}
def sudan_mem2(n, x, y):
    if (n, x, y) in memo:
        return memo[(n, x, y)]
    if n == 0:
        memo[(n, x, y)] = x+y
        return memo[(n, x, y)]
    if y == 0:
        memo[(n, x, y)] = x
        return memo[(n, x, y)]
    memo[(n, x, y)] = sudan_mem2(n-1, sudan_mem2(n, x, y-1), sudan_mem2(n, x, y-1) + y)
    return memo[(n, x, y)]


if __name__ == "__main__":

    sys.setrecursionlimit(5000)
    # Dla n = 0 będzie działało bardzo szybko [ O(n*m) ] niezależnie od wersji, bo sprowadza się do dodawania x+y
    tabliczka(1, 10, 1, 10, lambda x, y : sudan(0, x, y))

    # needs >30s to compute
    #tabliczka(0, 1, 0, 1, lambda x, y : sudan(1, x, y))
    print('sudan(1, 20, 20) = ', sudan(1, 20, 20))
    print('sudan_mem2(1, 20, 20) = ', sudan_mem2(1, 20, 20))

    # numbers grow really fast, so for values around (10^4, 10^4) wont work
    print('\n', 'sudan_mem2(1, 3000, 3000) = ', sudan_mem2(1, 3000, 3000), '\n\n')

    # works with memoization
    # for n > 2 naive version will take too long
    tabliczka(0, 3, 0, 2, lambda x, y : sudan_mem2(2, x, y))

    #version with memoization computes it in less than a second
    print('\n\n\n\n', 'sudan(2, 5, 2) = ', sudan_mem2(2, 5, 2))