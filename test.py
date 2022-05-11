def asks(k, n):
    def ingredients(func):
        def wrapper(*args, **kwargs):
            num = input(n)
            print(f"{k} = {num}")
            func(num)
        return wrapper
    return ingredients

def ask(k, n):
    def ingredients(func):
        def wrapper(*args, **kwargs):
            num = input(n)
            print(f"{k} = {num}")
            print(func(*args, num))
        return wrapper
    return ingredients
@asks('x', 'Enter first number: ')
@ask('y', 'Enter second number: ')
def calc(x, y):
    return int(x) + int(y)

calc()


# def calc(x, y):
#     print(f"{x}+{y}={int(x)+int(y)}")
#
# print(calc())