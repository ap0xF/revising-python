# Replace ___ with your code

# create the Coordinate class
class Coordinate:

    # initialize x and y attributes inside __init__()
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # define the add_coordinates() method
    def add_coordinates(self, c1: callable, c2: callable):
        c3 = Coordinate(c1.x + c2.x, c1.y + c2.y)
        return c3

    #     pass


# create objects c1 and c2
c1 = Coordinate(5, 6)
c2 = Coordinate(7, 9)

# call the add_coordinates() method
c3 = c2.add_coordinates(c1, c2)

# print attributes of the c3 object
print(c3.x)
print(c3.y)


t = set()
t.add(1)
t.add(2)
print(dir(t))
for i in t:
    print(i)

