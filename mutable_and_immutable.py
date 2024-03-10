lst1 = [1,2,3]
print(lst1)

# Mutable data types, can be changed / or changes inplace.
lst2 = lst1 # this is not creating a new list called lst2 and copying the value of lst1 to lst2
            # instead it is just creating a new pointer that points to same memory locaion as lst1 does.
            # so changing anyone will have effect on both the pointers

lst1.append(1)
print(lst1)

print(lst2) # this will also produce same output.
print(type(lst1))


# Immutable types
# numbers, string and tuple are immutable in python
# BEING IMMUATBLE DOESNOT MEAN IT CAN NOT BE REASSIGNED,
# IT MEANS ONCE A VALUE IS ASSIGNED YOU CANNOT EDIT THE ASSIGNED VALUE
# IT MUST BE REPLACED BY SOME OTHER COMPLETELY NEW VALUE.
x = 'str1 '
y = "st2"
print(x)
print(y)

try:
    x[0] = 'T'
except SyntaxError as e:
    print(e)


x = x+y
print(x)
