import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
exceptions = 'il1Lo0O'
chars = ''

name = input('Как тебя зовут? ')
print('Привет', name, 'я помогу тебе создать надежный пароль')

while True:
    pwd_quantity = input('Сколько паролей вам нужно сгенерировать? ')
    if pwd_quantity.isdigit() and float(pwd_quantity) - int(float(pwd_quantity)) == 0 and 1 <= int(pwd_quantity) <= 20:
        length = int(pwd_quantity)
        break
    else:
        print('А может быть все-таки введем целое число от 1 до 20? Иначе его могут легко взломать или ты сам можешь забыть!')

while True:
    pwd_len = int(input('Какой длины должен быть пароль? '))
    if 5 < int(pwd_len) < 20:
        break
    elif 6 > int(pwd_len):
        print('Боюсь, для надежного пароля этого не хватит ')
    elif int(pwd_len) > 20:
        print('Такой большой пароль и забыть не долго ')

while True:
    pwd_digits = input('Включать ли в пароль цифры от 0 до 9? ')
    if pwd_digits not in ('да', 'д', 'н', 'нет', 'l', 'lf', 'y', 'ytn'):
        print('Кажется ты не можешь нащупать нужные буквы ')
        pwd_digits = input('Давай еще раз, включать ли в пароль цифры от 0 до 9? ')
    elif pwd_digits in ('да', 'д', 'l', 'lf'):
        chars += digits
        break
    elif pwd_digits in ('н', 'нет', 'y', 'ytn'):
        break

while True:
    pwd_uppercase = input('Включать ли в пароль прописные буквы? ')
    if pwd_uppercase not in ('да', 'д', 'н', 'нет', 'l', 'lf', 'y', 'ytn'):
        print('Кажется ты не можешь нащупать нужные буквы ')
        pwd_uppercase = input('Давай еще раз, включать ли в пароль цифры от 0 до 9? ')
    elif pwd_uppercase in ('да', 'д', 'l', 'lf'):
        chars += uppercase_letters
        break
    elif pwd_uppercase in ('н', 'нет', 'y', 'ytn'):
        break

while True:
    pwd_lowercase = input('Включать ли в пароль строчные буквы? ')
    if pwd_lowercase not in ('да', 'д', 'н', 'нет', 'l', 'lf', 'y', 'ytn'):
        print('Кажется ты не можешь нащупать нужные буквы ')
        pwd_lowercase = input('Давай еще раз, включать ли в пароль цифры от 0 до 9? ')
    elif pwd_lowercase in ('да', 'д', 'l', 'lf'):
        chars += lowercase_letters
        break
    elif pwd_lowercase in ('н', 'нет', 'y', 'ytn'):
        break

while True:
    pwd_punctuation = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? ')
    if pwd_punctuation not in ('да', 'д', 'н', 'нет', 'l', 'lf', 'y', 'ytn'):
        print('Кажется ты не можешь нащупать нужные буквы ')
        pwd_punctuation = input('Давай еще раз, включать ли в пароль цифры от 0 до 9? ')
    elif pwd_punctuation in ('да', 'д', 'l', 'lf'):
        chars += punctuation
        break
    elif pwd_punctuation in ('н', 'нет', 'y', 'ytn'):
        break

while True:
    pwd_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"? ')
    if pwd_exceptions not in ('да', 'д', 'н', 'нет', 'l', 'lf', 'y', 'ytn'):
        print('Кажется ты не можешь нащупать нужные буквы ')
        pwd_exceptions = input('Давай еще раз, включать ли в пароль цифры от 0 до 9? ')
    elif pwd_exceptions in ('да', 'д', 'l', 'lf'):
        chars += exceptions
        break
    elif pwd_exceptions in ('н', 'нет', 'y', 'ytn'):
        break

def create():
    for i in range(length):
        print('Пароль', i + 1, ':')
        print(*random.sample(chars, pwd_len), sep='')

create()