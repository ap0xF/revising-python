import time

#
# x = [i for i in range(10)]
# print(x)

# this code will create 10 empty lists inside a parent list
# these all of the lists are distinct lists.
# y = [[] for i in range(10)]
# print(y)


# Lets Compare between tradional for loop and list comprehension.

# def timer(fx):
#     def wrapper():
#         start_time = time.time()
#         fx()
#         end_time = time.time()
#         print(f'{fx.__name__} took {(end_time - start_time)} time.')
#         return fx()
#
#     return wrapper()
#
#
# @timer
# def creating_a_list_using_list_comprehension():
#     sq = [x ** 2 for x in range(10_000_0000)]
#     return sq
#
# @timer
# def creating_a_list_using_for_loop():
#     manual_sq = []
#     for i in range(10_000_0000):
#         manual_sq.append(i ** 2)
#     return manual_sq

#
# z = [[j for j in range(5) if j % 2 == 0] for i in range(10)]
# print(z)

"""One more example of List Comprehension"""
combination = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6] if x!=y]
print(combination)
