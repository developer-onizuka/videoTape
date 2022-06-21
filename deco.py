def deco(func):
    def wrapper(arg):
        print('----- start -----')
        print(func(arg))
        print('----- end -----')
    return wrapper


def hello(str):
    return str 

decorated_hello = deco(hello)
decorated_hello("Hello World!")
