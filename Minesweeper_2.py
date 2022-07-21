# Для начала в программе объявите класс GamePole, который будет создавать и управлять игровым полем. Объект этого класса должен формироваться командой:
#
# pole = GamePole(N, M, total_mines)
# И, так как поле в игре одно, то нужно контролировать создание только одного объекта класса GamePole (используйте паттерн Singleton, о котором мы с вами говорили, когда рассматривали магический метод __new__()).
#
# Объект pole должен иметь локальный приватный атрибут:
#
# __pole_cells - двумерный (вложенный) кортеж, размерами N x M элементов (N строк и M столбцов), состоящий из объектов класса Cell.
#
# Для доступа к этой коллекции объявите в классе GamePole объект-свойство (property):
#
# pole - только для чтения (получения) ссылки на коллекцию __pole_cells.
#
# Далее, в самом классе GamePole объявите следующие методы:
#
# init_pole() - для инициализации начального состояния игрового поля (расставляет мины и делает все клетки закрытыми);
# open_cell(i, j) - открывает ячейку с индексами (i, j); нумерация индексов начинается с нуля; метод меняет значение атрибута __is_open объекта Cell в ячейке (i, j) на True;
# show_pole() - отображает игровое поле в консоли (как именно сделать - на ваше усмотрение, этот метод - домашнее задание).
#
# Расстановку мин выполняйте случайным образом по игровому полю (для этого удобно воспользоваться функцией randint модуля random). После расстановки всех total_mines мин, вычислите их количество вокруг остальных клеток (где нет мин). Область охвата - соседние (прилегающие) клетки (8 штук).
#
# В методе open_cell() необходимо проверять корректность индексов (i, j). Если индексы указаны некорректно, то генерируется исключение командой:
#
# raise IndexError('некорректные индексы i, j клетки игрового поля')
# Следующий класс Cell описывает состояние одной ячейки игрового поля. Объекты этого класса создаются командой:
#
# cell = Cell()
# При этом в самом объекте создаются следующие локальные приватные свойства:
#
# __is_mine - булево значение True/False; True - в клетке находится мина, False - мина отсутствует;
# __number - число мин вокруг клетки (целое число от 0 до 8);
# __is_open - флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.
#
# Для работы с этими приватными атрибутами объявите в классе Cell следующие объекты-свойства с именами:
#
# is_mine - для записи и чтения информации из атрибута __is_mine;
# number - для записи и чтения информации из атрибута __number;
# is_open - для записи и чтения информации из атрибута __is_open.
#
# В этих свойствах необходимо выполнять проверку на корректность переданных значений (либо булево значение True/False, либо целое число от 0 до 8). Если передаваемое значение некорректно, то генерировать исключение командой:
#
# raise ValueError("недопустимое значение атрибута")
# С объектами класса Cell должна работать функция:
#
# bool(cell)
# которая возвращает True, если клетка закрыта и False - если открыта.
#
# Пример использования классов (эти строчки в программе писать не нужно):
#
# pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
# pole.init_pole()
# if pole.pole[0][1]:
#     pole.open_cell(0, 1)
# if pole.pole[3][5]:
#     pole.open_cell(3, 5)
# pole.open_cell(30, 100)  # генерируется исключение IndexError
# pole.show_pole()


import random


class Cell:
    def __init__(self, is_mine=False, number=0, is_open=False):
        self.__is_mine = is_mine
        self.__number = number
        self.__is_open = is_open

    def __bool__(self):
        if self.is_open:
            return False
        return True

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, new):
        if not isinstance(new, bool):
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = new

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, new):
        if new < 0 or new > 8:
            raise ValueError("недопустимое значение атрибута")
        self.__number = new

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, new):
        if not isinstance(new, bool):
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = new



class GamePole:
    count = 0
    __instance = None

    def __new__(cls, *args, **kwargs):
        cls.count += 1
        if cls.count < 2:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        elif cls.count >= 2:
            return cls.__instance

    def __init__(self, N, M, total_mines):
        self.n = N
        self.m = M
        self.total_mines = total_mines
        self.__pole_cells = [[Cell() for _ in range(self.m + 2)] for _ in range(self.n + 2)]

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        #self.pole = [[Cell() for i in range(self.n + 2)] for i in range(self.m + 2)]

        rng = random.Random()
        while self.total_mines > 0:
            i = rng.randrange(1, self.n + 1)
            j = rng.randrange(1, self.m + 1)
            if self.__pole_cells[i][j].is_mine != False:
                continue
            self.__pole_cells[i][j].is_mine = True
            self.total_mines -= 1

        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                k = 0
                if self.__pole_cells[i][j].is_mine != True:
                    if self.__pole_cells[i][j + 1].is_mine:
                        k += 1
                    if self.__pole_cells[i + 1][j + 1].is_mine:
                        k += 1
                    if self.__pole_cells[i + 1][j].is_mine:
                        k += 1
                    if self.__pole_cells[i][j - 1].is_mine:
                        k += 1
                    if self.__pole_cells[i + 1][j - 1].is_mine:
                        k += 1
                    if self.__pole_cells[i - 1][j - 1].is_mine:
                        k += 1
                    if self.__pole_cells[i - 1][j + 1].is_mine:
                        k += 1
                    if self.__pole_cells[i - 1][j].is_mine:
                        k += 1
                    self.__pole_cells[i][j].number = k

        self.__pole_cells = self.__pole_cells[1:self.n + 1]
        for i in range(self.n):
            self.__pole_cells[i].pop(0)
            self.__pole_cells[i].pop(-1)

    def open_cell(self, i, j):
        if i < 0 or i >= self.n or j < 0 or j >= self.m:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.__pole_cells[i][j].is_open = True


    def show_pole(self):
        for i in range(self.n):
            for j in range(self.m):
                print(str(self.__pole_cells[i][j].number).rjust(3), end=' ')
            print()

        for i in range(self.n):
            for j in range(self.m):
                print(str(self.__pole_cells[i][j].is_mine).rjust(3), end=' ')
            print()


pole = GamePole(10, 20, 10)
pole.init_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
#pole.open_cell(9, 19)  # генерируется исключение IndexError
pole.show_pole()

p1 = GamePole(10, 20, 10)
p2 = GamePole(10, 20, 10)
assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
p = p1

cell = Cell()
assert type(Cell.is_mine) == property and type(Cell.number) == property and type(
    Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

cell.is_mine = True
cell.number = 5
cell.is_open = True
assert bool(cell) == False, "функция bool() вернула неверное значение"

try:
    cell.is_mine = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    cell.number = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

p.init_pole()
m = 0
for row in p.pole:
    for x in row:
        assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
        if x.is_mine:
            m += 1

assert m == 10, "на поле расставлено неверное количество мин"
p.open_cell(0, 1)
p.open_cell(9, 19)

try:
    p.open_cell(10, 20)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"


def count_mines(pole, i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k + i, l + j
            if ii < 0 or ii > 9 or jj < 0 or jj > 19:
                continue
            if pole[ii][jj].is_mine:
                n += 1

    return n


for i, row in enumerate(p.pole):
    for j, x in enumerate(row):
        if not p.pole[i][j].is_mine:
            m = count_mines(p.pole, i, j)
            assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"