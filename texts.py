print('C:\\some\\name')  # here \n means newline!

# If you dont want characters prefaced by \ to be interpreted as special characters,
# you can use raw strings by adding an r before the first quote:
print(r'C:\some\name')  # note the r before the quote

# but there is small issue with using raw strings and that is
# 
# print(r'this\will\work\') # this will throw error saying string literal is not terminated.


# workarounds for this will be.
print("this\\can\\be\\done\\like\\this\\")

# string repeatation can also be done using * operator
print(3 * 'un' + 'ium')

# Two or more string literals (i.e. the ones enclosed between quotes)
# next to each other are automatically concatenated.
print('hell' 'oh')

# test = "hell"
# print(test'o')  # throws syntax error, joining

word = [1, 2, 3, 4, 5, 6]

print(word[6:42]) # prints '[]', indexing handles IndexError gracefully.
# print(word[42]) #this will throw IndexError

# in python numbers, strings and tuples are immutable.
# they can be re-defined but cannot be changed

x = 223
# x[0] = 3 # not valid


