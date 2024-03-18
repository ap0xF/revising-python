import random


# def fib(count: int):
#     a, b = 1, 0
#     for _ in range(count):
#         a, b = b, a + b
#         yield b
#
#
# result_decorator = fib(5)
# try:
#     while True:
#         print(next(result_decorator))
# except StopIteration:
#     pass


# another example of using yield keyword
def counter(start=0):
    value = start
    while True:
        value += yield value
    # yield value


def main():
    gen = counter(10)
    print(next(gen))

