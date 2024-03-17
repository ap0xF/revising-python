class Test:
    x = [20, 30]

    # def __init__(t):
    #     x = set()
    #     t.x.append(20)
    #     print(t.x)
    #     x.add(30)
    #     print(x)

    # def __init__(t, z): # there is no support for construcor overloading in py, instead we can do as done below in nxt
    # funcn

    #     x = set()
    #     t.x.append(20)
    #     print(t.x)
    #     x.add(30)
    #     print(x)

    # an example of constructor with nullable params, a gmimck of constructor overloading
    def __init__(self, name=None, address=None, phone_number=None, email=None, salary=None, wife_name=None):
        self.name = "Aadit"
        print(name, address, phone_number, x)

    def a_method(self):
        print(self.name)
        print(self.name)
        return "Teska Baje"


t = Test()
# print(Test.a_method(self="fu"))
print(t.a_method())


x = Test()
print(Test.a_method(self=x))
