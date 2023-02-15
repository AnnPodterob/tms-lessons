def my_decorator(function):
    def else_func(a):
        print(a)
        b = function(a)
        print(b)
        return b
    return else_func

@my_decorator
def my_funct(a):
    return a ** 3

c = my_funct(4)
print(c)