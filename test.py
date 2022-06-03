# Cell - для представления клетки игрового поля;
# GamePole - для управления игровым полем, размером N x N клеток.
#
# С помощью класса Cell предполагается создавать отдельные клетки командой:
#
# c1 = Cell(around_mines, mine)
# Здесь around_mines - число мин вокруг данной клетки поля; mine - булева величина (True/False), означающая наличие мины в текущей клетке. При этом, в каждом объекте класса Cell должны создаваться локальные свойства:
#
# around_mines - число мин вокруг клетки (начальное значение 0);
# mine - наличие мины в текущей клетке (True/False);
# fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False).
#
# С помощью класса GamePole должна быть возможность создавать квадратное игровое поле с числом клеток N x N:
#
# pole_game = GamePole(N, M)
# Здесь N - размер поля; M - общее число мин на поле. При этом, каждая клетка представляется объектом класса Cell и все объекты хранятся в двумерном списке N x N элементов - локальном свойстве pole объекта класса GamePole.
#
# В классе GamePole должны быть также реализованы, следующие методы:
#
# init() - инициализация поля с новой расстановкой M мин (случайным образом по игровому полю, разумеется каждая мина должна находиться в отдельной клетке).
# show() - отображение поля в консоли в виде таблицы чисел открытых клеток (если клетка не открыта, то отображается символ #).
#
# При создании экземпляра класса GamePole в его инициализаторе следует вызывать метод init() для первоначальной инициализации игрового поля.
#
# В классе GamePole могут быть и другие вспомогательные методы.
#
# Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом мин M = 12. Вызовите метод init() для расстановки мин по игровому полю и подсчета числа мин вокруг клеток без мин.

import random


class Ceil:
    def __init__(self, around_mines, mine):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def init(self):
        self.pole = [[Ceil(0, False) for i in range(self.n+2)] for i in range(self.n+2)]

        rng = random.Random()
        while self.m > 0:
            i = rng.randrange(1, self.n+1)
            j = rng.randrange(1, self.n+1)
            if self.pole[i][j].mine != False:
                continue
            self.pole[i][j].mine = True
            self.m -= 1

        for i in range(1, self.n + 1):
            for j in range(1, self.n + 1):
                k = 0
                if self.pole[i][j + 1].mine == True:
                    k += 1
                if self.pole[i + 1][j + 1].mine == True:
                    k += 1
                if self.pole[i + 1][j].mine == True:
                    k += 1
                if self.pole[i][j - 1].mine == True:
                    k += 1
                if self.pole[i + 1][j - 1].mine == True:
                    k += 1
                if self.pole[i - 1][j - 1].mine == True:
                    k += 1
                if self.pole[i - 1][j + 1].mine == True:
                    k += 1
                self.pole[i][j].around_mines = k


    def show(self):
        for i in range(1, self.n+1):
            for j in range(1, self.n+1):
                print(str(self.pole[i][j].around_mines).rjust(3), end=' ')
            print()
        print()
        for i in range(1, self.n + 1):
            for j in range(1, self.n + 1):
                print(str(self.pole[i][j].mine).rjust(3), end=' ')
            print()


pole_game = GamePole(10, 12)
pole_game.init()
pole_game.show()