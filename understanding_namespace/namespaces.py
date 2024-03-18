def check_namespace(obj):
    if obj in globals().values():
        return "global"
    elif obj in locals().values():
        return "local"
    else:
        return "unknown"


x = 10  # global variable


def test():
    y = 20  # local variable
    print(check_namespace(y))  # Prints: local


test()
print(check_namespace(x))  # Prints: global
