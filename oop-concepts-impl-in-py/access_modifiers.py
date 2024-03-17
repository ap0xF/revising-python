class MyClass:
    public_v = "this is a convention to define public variable"
    _protected_v = "this is a convention to define public variable"
    __private_v = 'it is private'


my_obj = MyClass()
print(my_obj.public_v)
print(MyClass.public_v)

print(my_obj._protected_v)
print(MyClass._protected_v)



print(my_obj._MyClass__private_v)
print(MyClass._MyClass__private_v)


"""“Name mangling” is about safety, not security: 
it’s designed to prevent accidental access and not intentional wrongdoing.”"""