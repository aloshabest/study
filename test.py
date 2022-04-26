# Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age.
# По умолчанию name = Ivan, age = 18, groupNumber = 10A.
# Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge, setGroupNumber.
# Метод getName нужен для получения данных об имени конкретного студента, метод getAge нужен для получения данных о возрасте конкретного студента,
# vетод setGroupNumberнужен для получения данных о номере группы конкретного студента.
# Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, метод setGroupNumber позволяет изменить номер группы установленный по умолчанию.
# В программе необходимо создать пять экземпляров класса Student, установить им разные имена, возраст и номер группы.


class Student:

    def __init__(self, name='Ivan', age=18, groupNumber='10A'):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, name):
        self.name = name

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber

s1 = Student('Dmitry', 22, '11Б')
s2 = Student('Ivan', 15, '7Б')

print(s1.getGroupNumber())
print(s2.getName())
print(s2.getGroupNumber())
s2.setGroupNumber('8Б')
print(s2.getGroupNumber())





print()
print('------------------------------------')
print()


# Напишите программу с классом Car. Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
# Напишите пять методов. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен». Второй — отключение автомобиля — выводит сообщение
# «Автомобиль заглушен». Третий — присвоение автомобилю года выпуска. Четвертый метод — присвоение автомобилю типа. Пятый — присвоение автомобилю цвета.


class Car:

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def on(self):
        return 'Автомобиль заведен'

    def off(self):
        return 'Автомобиль заглушен'

    def year(self, year):
        self.year = year

    def color(self, color):
        self.color = color

    def type(self, type):
        self.type = type

c1 = Car('black', 'SUV', 1985)
print(c1.type)
print(c1.on())





