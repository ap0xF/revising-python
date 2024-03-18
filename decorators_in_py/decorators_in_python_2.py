from typing import Callable


def greet(fx: Callable):
    def m_fx():
        print("Good Morning")
        print(fx())
        print(f"Thank you for using {fx.__name__} function")
    # return m_fx() # m_fx is being called here
    return m_fx()


@greet
def hello():
    return "Hello World"

# temp = greet(hello)
# print(temp)
