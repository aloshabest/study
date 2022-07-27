# В программе необходимо реализовать таблицу TableValues по следующей схеме:
# Сам класс TableValues представляет таблицу в целом, объекты которого создаются командой:
#
# table = TableValues(rows, cols, type_data)
# где rows, cols - число строк и столбцов таблицы; type_data - тип данных ячейки (int - по умолчанию, float, list, str и т.п.). Начальные значения в ячейках таблицы равны 0 (целое число).
#
# Каждая ячейка таблицы должна быть представлена классом Cell. Объекты этого класса создаются командой:
#
# cell = Cell(data)
# где data - данные в ячейке. В каждом объекте класса Cell должен формироваться локальный приватный атрибут __data с соответствующим значением. Для работы с ним в классе Cell должно быть объект-свойство (property):
#
# data - для записи и считывания информации из атрибута __data.
#
# При попытке записать данные другого типа (не совпадающего с атрибутом type_data объекта класса TableValues), должно генерироваться исключение командой:
#
# raise TypeError('неверный тип присваиваемых данных')
# С объектами класса TableValues должны выполняться следующие команды:
#
# table[row, col] = value# запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
# value = table[row, col] # считывание значения из ячейки с индексами row, col
#
# for row in table:  # перебор по строкам
#     for value in row: # перебор по столбцам
#         print(value, end=' ')  # вывод значений ячеек в консоль
#     print()
# При работе с индексами row, col, необходимо проверять их корректность. Если индексы не целое число или они выходят за диапазон размера таблицы, то генерировать исключение командой:
#
# raise IndexError('неверный индекс')

class Cell:
    def __init__(self, data=0, next=None):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, obj):
        self.__data = obj


class TableValues:
    def __init__(self, rows=0, cols=0, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.cells = tuple(tuple(Cell() for j in range(cols)) for i in range(rows))

    def check(self, key):
        key1, key2 = key
        if not (0 <= key1 < self.rows) or not (0 <= key2 < self.cols):
            raise IndexError('неверный индекс')
        return True

    def __setitem__(self, key, value):
        self.check(key)
        if type(value) != self.type_data:
            raise TypeError('неверный тип присваиваемых данных')
        r, c = key
        self.cells[r][c].data = value

    def __getitem__(self, indx):
        self.check(indx)
        r, c = indx
        return self.cells[r][c].data

    def __iter__(self):
        for i in self.cells:
            yield (j.data for j in i)
