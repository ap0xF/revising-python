# Simple assignment in Python never copies data. 
# When you assign a list to a variable, the variable refers to the existing list. 
# Any changes you make to the list through one variable will be seen 
# through all other variables that refer to it
lst = [1, 2, 3, 4, 5]
lst1 = lst
lst1.append(6)
print(lst1)
print(lst)

# slcie operation returns a new list containing
# requested elements
# it does shallow copy.
rgb = ["Red", "Green", "Blue"]
rgba = rgb[:]  # this does a shallow copy.
rgba.append("Alpha")
print(rgb)
print(rgba)

# suppose if we have a list inside of list
lst2 = [3, 4, 5]
lst3 = [1, 2, lst2]

# now if i do shallow copy of lst3 to a new lst4
lst4 = lst3[:]
# and if I change the data inside of lst2 via lst4 then
# for both lst3 and lst4 the data inside of lst2 is changed
# this is beacause of shallow copy bheaviour.
