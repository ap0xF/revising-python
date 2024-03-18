import random
import time


# in python, functions and classes are first class citizens.
# in programming : first class citizen are anything that can be
# passed as a regular datatypes.

# def compose(f,g,x):
#     return(f(g(x)))

# compose(print, len, "Hello")


# nesting the functions
# in python functions are first class citizens that can be nested.
# def random_power():
#     def f(x):
#         return x**2
#     def g(x):
#         return x**3
#     def h(x):
#         return x**4

#     functions = [f,g,h]
#     return random.choice(functions)

# for i in range(1):
#     p = random_power()
#     print(p)
#     print(p(3))


# now, let's use these above learning to create a decorator called timer


def timer(f):
    def wrapper(*args):
        start_time: float = time.time()
        result: dict = f(*args)
        end_time = time.time()
        dt = end_time - start_time
        print(dt)
        return result

    return wrapper


@timer
def prime_factorization(n):
    factors = set()  # defining an empty set in py.
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            n //= divisor
        divisor += 1
        factors.add(divisor)

    return factors
# test





#
# prime_factorization_timer = timer(prime_factorization)
#
# result = prime_factorization_timer(27)
#
# print(result)
#
# name: str = "Hello"
