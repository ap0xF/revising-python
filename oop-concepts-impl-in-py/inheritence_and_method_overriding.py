class Shape:
    def __init__(self, name, description):
        self.shape_name = name
        self.shape_description = description

    def get_details(self):
        return {"Name": self.shape_name, "Description": self.shape_description}

    def area(self, length, breadth):
        return length*breadth

    def perimeter(self, length, breadth):
        pass


# Creating a sub-class called, Cirlce which inherits class Called shape
# class Circle(Shape):
#     def __init__(self, name, description):
#         super().__init__(name, description)


print(dir(Shape))
