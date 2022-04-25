#Запоминание принятых аргументов и вывод без надписи Calculating...
#Дополнен ограничением в 3 значения

from functools import wraps

def memoized(n):
    memory = {}
    def wrapper(func):
        @wraps(func)
        def inner(*args):
            if args not in memory:
                memory[args] = func(*args)
            if len(memory) == n:
                memory.pop(list(memory)[0])
            return memory[args]
        return inner
    return wrapper

@memoized(3)
def f(x):
    print("Calculating...")
    return x * 10


print(f(1))
print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(1))

