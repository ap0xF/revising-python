x = [i for i in range(10)]
print(x)

# these all of the lists are distinct lists.
y = [[] for i in range(10)]
print(y)

z = [[j for j in range(5) if j % 2 == 0] for i in range(10)]
print(z)