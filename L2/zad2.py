# returns floor(sqrt(n))

from cmath import sqrt


def sqroot_approx(n):
    res, i  = 0, 0
    while res <= n:
        i += 1
        res += 2*i-1
        
    return i-1


if __name__ == "__main__":
    
    s = 50
    n = 100
    for i in range(s, n+1):
        print(f'floor(sqrt({i})) = {sqroot_approx(i)}  sqrt({i}) ≈ {i**0.5}')