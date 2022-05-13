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





print()
print('------------------------------------')
print()



# Разработайте программу по следующему описанию.
# В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный номер объекта, и свойство, в котором хранится принадлежность команде.
# У солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа "герой". У героев есть метод увеличения собственного уровня.
# В основной ветке программы создается по одному герою для каждой команды. В цикле генерируются объекты-солдаты. Их принадлежность команде определяется случайно.
# Солдаты разных команд добавляются в разные списки.
# Измеряется длина списков солдат противоборствующих команд и выводится на экран. У героя, принадлежащего команде с более длинным списком, увеличивается уровень.
# Отправьте одного из солдат первого героя следовать за ним. Выведите на экран идентификационные номера этих двух юнитов.


import random


class Unit:
    def __init__(self, number, commandid):
        self.number = number
        self.commandId = commandid


class Hero(Unit):
    def __init__(self,  number, commandid, name, level=1):
        Unit.__init__(self, number, commandid)
        self.name = name
        self.level = level

    def getlevel(self):
        return self.level

    def inclevel(self):
        self.level += 1
        print(f"Уровень героя {self.name} увеличен на 1 и равен {self.level}")


class Soldier(Unit):
    def gotohero(self, Hero):
        print(f"Солдат номер {self.number} следует за героем {Hero.name}, имеющим номер {Hero.number}")


def lvlUp(armyH1, armyH2):
    if len(armyH1) > len(armyH2):
        print(f"В армии {H1.name} больше солдат, поэтому его уровень растет!")
        return H1.inclevel()
    print(f"В армии {H2.name} больше солдат, поэтому его уровень растет!")
    return H2.inclevel()



H1 = Hero(1, 1, 'Ахиллес')
H2 = Hero(2, 2, 'Гектор')
armyH1, armyH2 = [], []

for i in range(3, 14):
    n = random.randint(0, 1)
    if n:
        armyH1.append(Soldier(i, 1))
        print(f"Солдат с номером {i} добавлен в армию {H1.name}")
    else:
        armyH2.append(Soldier(i, 2))
        print(f"Солдат с номером {i} добавлен в армию {H2.name}")

print(f"Армия героя {H1.name}: {len(armyH1)}")
print(f"Армия героя {H2.name}: {len(armyH2)}")

lvlUp(armyH1, armyH2)

armyH1[1].gotohero(H1)



print()
print('------------------------------------')
print()


# В качестве практической работы попробуйте самостоятельно перегрузить оператор сложения. Для его перегрузки используется метод __add__().
# Он вызывается, когда объекты класса, имеющего данный метод, фигурируют в операции сложения, причем с левой стороны.
# Это значит, что в выражении a + b у объекта a должен быть метод __add__(). Объект b может быть чем угодно, но чаще всего он бывает объектом того же класса.
# Объект b будет автоматически передаваться в метод __add__() в качестве второго аргумента (первый – self).

class Number_one:

    def __init__(self):
        pass

    def __add__(self, other):
        other = Number_one()
        return other

class Number_two:

    def __init__(self):
        pass

a = Number_one()
b = Number_two()
c = a + b
print(a, b, c)



print()
print('------------------------------------')
print()

