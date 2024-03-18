# list is an iterable but not an iterator
# to be iterator an object must have two dunder methods
# __iter__ and __next__

# iterable has __iter__ dunder method but it does not have
# __next__ dunder method, which means it cannot get next value as it doesnot know
# where the iteration is curretly at aka state

nums = [1, 2, 3, 4, 5]




lst = dir(nums)
has_iter = False
has_next = False
is_iterator = False

for i in lst:
    if i == '__iter__':
        has_iter = True
    if i == '__next__':
        has_next = True

    is_iterator = has_iter and has_next

if is_iterator:
    print(f'Given {type(nums)} is an iterator')

print(f'Given {type(nums)} is not an iterator')



