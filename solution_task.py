# Декоратор asks() добавляет описание одного из аргументов преобразуемой функции. Для каждого аргумента нужен будет отдельный вызов asks().
# Важный момент: порядок появления запросов во время диалога с пользователем должен соответствовать порядку расположения декораторов в файле
# (а не порядку их фактического применения) — смотрите пример ниже.
# После того, как все аргументы преобразуемой функции будут описаны с помощью asks(), применяется декоратор interactive().
# После его применения результирующая функция перестаёт принимать аргументы и возвращать результат (None в итоге возвращается, конечно),
# зато начинает общаться с пользователем.
# Обе функции в модуле уже объявлены, но не реализованы. Вам нужно будет написать "тела" этих функций. Обе функции снабжены docstrings
# (в порядке исключения — на русском языке), которые поясняют назначение аргументов каждой функции.
#
#
# @interactive('Calculator')
# @asks('x', 'Enter first number: ')
# @asks('y', 'Enter second number: ')
# def calc(x, y):
#     return int(x) + int(y)
#
# calc()
# Calculator
# Enter first number: 42
# Enter second number: 57
# # 99



def interactive(x):
    def bread(func):
        def wrapper():
            print(x)
            func()
        return wrapper
    return bread

def asks(k, n):
    def ingredients(func):
        def wrapper(*args):
            num = input(n)
            print(f"{k} = {num}")
            print(f'{func(*args, num)}')
            return ''
        return wrapper
    return ingredients

@interactive('Calculator')
@asks('x', 'Enter first number: ')
@asks('y', 'Enter second number: ')
def calc(x, y):
   return int(x)+int(y)

calc()





