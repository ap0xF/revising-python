import logging

# configuring logging, to log to console
logging.basicConfig(level=logging.DEBUG)


def log(fx):
    def wrapper(*args):
        logging.info(f'The name of funcn is {fx}')
        logging.info(f'the arguments passed to the funcn are:- {args}')
        res = fx()
        logging.info(f'The return value of funcn {fx} is :- {res} and is of type:- {type(res)}')
        print(res)

    return wrapper

@log
def test_me():
    return "I am tested"


test_me()
