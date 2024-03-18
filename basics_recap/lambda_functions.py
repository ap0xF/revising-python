lambda x,y:x+y # a simple lambda function which takes x and y as an argument and returns sum of them.

#using lambda funcn
print((lambda x,y:x+y)(5,4))


# lamda funcn are mostly used in higher order funcn ( funcn which takes other funcn as param and/or returns some function)

def my_map(my_func, my_item):
    result = []
    for item in my_item:
        new_item = my_func(item)
        result.append(new_item)
    return result

iterable = [1,2,3,4,5]

res = my_map(lambda x : x**2, iterable)
print(res)




# map funcn in py

def take_out_even(lst):
    new_lst = []
    for i in lst:
        if i%2 == 0:
            new_lst.append(i)

lst = [1,2,3,4,5,6,7,8,9]
new_lst = map(take_out_even, lst)
print(new_lst)