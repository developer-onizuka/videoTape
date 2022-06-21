def deco(func):
    def wrapper(arg):
        print('----- start -----')
        print(func(arg))
        print('----- end -----')
    return wrapper

@deco
def hello(str):
    return str 


hello("Hello World!")
