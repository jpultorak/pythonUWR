from itertools import product

def solve(s1, s2, res_string, allow_leading0 = False):

    nums = [i for i in range(0, 10)]
    letters = [letter for letter in set(s1+s2+res_string)]
    total_letters = len(letters)

    for val in product(nums, repeat=total_letters):

        f = dict(zip(letters, val))
        if not allow_leading0 and f[s1[0]] == 0 or f[s2[0]] == 0 or f[res_string[0]] == 0:
            continue

        num1 = 0
        num2 = 0
        res = 0

        for power, letter in enumerate(reversed(s1)):
            num1 += f[letter]*(10**power)
        for power, letter in enumerate(reversed(s2)):
            num2 += f[letter]*(10**power)
        for power, letter in enumerate(reversed(res_string)):
            res += f[letter]*(10**power)
        if num1+num2 == res:
            yield f
            pass

# works but takes a few minutes
""" for res in solve(lambda x, y : x+y, "SEND", "MORE", "MONEY"):
    print(res) """
#print all solutions
for res in solve(lambda x, y : x+y, "KIOTO", "OSAKA", "TOKIO"):
    print(res, '\n')

# get six solutions
puzzle =  solve(lambda x, y : x+y, "TRZY", "TRZY", "SZEŚĆ")
for i in range(10):
    print(next(puzzle), '\n')
