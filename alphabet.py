# Класс Alphabet
# Создайте класс Alphabet
# Создайте метод __init__(), внутри которого будут определены два динамических свойства: 1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
# Создайте метод print(), который выведет в консоль буквы алфавита
# Создайте метод letters_num(), который вернет количество букв в алфавите
#
# Класс EngAlphabet
# Создайте класс EngAlphabet путем наследования от класса Alphabet
# Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__(). В качестве параметров ему будут передаваться обозначение языка(например, 'En') и строка, состоящая из всех букв алфавита(можно воспользоваться свойством ascii_uppercase из модуля string).
# Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите.
# Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять, относится ли эта буква к английскому алфавиту.
# Переопределите метод letters_num() - пусть в текущем классе классе он будет возвращать значение свойства __letters_num.
# Создайте статический метод example(), который будет возвращать пример текста на английском языке.
#
# Тесты:
# Создайте объект класса EngAlphabet
# Напечатайте буквы алфавита для этого объекта
# Выведите количество букв в алфавите
# Проверьте, относится ли буква F к английскому алфавиту
# Проверьте, относится ли буква Щ к английскому алфавиту
# Выведите пример текста на английском языке
import string

class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)

    def print(self):
        print(f"{self.letters}")

    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):

    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def is_en_letter(self, word):
        if word.upper() in self.letters:
            return True
        return False

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        print("English Example:\nDon't judge a book by it's cover.")


words = EngAlphabet()

words.print()

print(words.letters_num())

print(words.is_en_letter('F'))

print(words.is_en_letter('Щ'))

words.example()