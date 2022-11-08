import timeit
def foo():
    print("here is my code to time...")


timeit.timeit(stmt=foo, number=1234567)