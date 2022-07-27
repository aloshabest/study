# Объявите класс Matrix (матрица) для операций с матрицами. Объекты этого класса должны создаваться командой:
#
# m1 = Matrix(rows, cols, fill_value)
# где rows, cols - число строк и столбцов матрицы; fill_value - заполняемое начальное значение элементов матрицы (должно быть число: целое или вещественное). Если в качестве аргументов передаются не числа, то генерировать исключение:
#
# raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
# Также объекты можно создавать командой:
#
# m2 = Matrix(list2D)
# где list2D - двумерный список (прямоугольный), состоящий из чисел (целых или вещественных). Если список list2D не прямоугольный, или хотя бы один из его элементов не число, то генерировать исключение командой:
#
# raise TypeError('список должен быть прямоугольным, состоящим из чисел')
# Для объектов класса Matrix должны выполняться следующие команды:
#
# matrix = Matrix(4, 5, 0)
# res = matrix[0, 0] # возвращается первый элемент матрицы
# matrix[indx1, indx2] = value # элементу матрицы с индексами (indx1, indx2) присваивается новое значение
# Если в результате присвоения тип данных не соответствует числу, то генерировать исключение командой:
#
# raise TypeError('значения матрицы должны быть числами')
# Если указываются недопустимые индексы матрицы (должны быть целыми числами от 0 и до размеров матрицы), то генерировать исключение:
#
# raise IndexError('недопустимые значения индексов')
# Также с объектами класса Matrix должны выполняться операторы:
#
# matrix = m1 + m2 # сложение соответствующих значений элементов матриц m1 и m2
# matrix = m1 + 10 # прибавление числа ко всем элементам матрицы m1
# matrix = m1 - m2 # вычитание соответствующих значений элементов матриц m1 и m2
# matrix = m1 - 10 # вычитание числа из всех элементов матрицы m1
# Во всех этих операция должна формироваться новая матрица с соответствующими значениями. Если размеры матриц не совпадают (разные хотя бы по одной оси), то генерировать исключение командой:
#
# raise ValueError('операции возможны только с матрицами равных размеров')
# Пример для понимания использования индексов (эти строчки в программе писать не нужно):
#
# mt = Matrix([[1, 2], [3, 4]])
# res = mt[0, 0] # 1
# res = mt[0, 1] # 2
# res = mt[1, 0] # 3
# res = mt[1, 1] # 4




class Matrix:
    def __init__(self, *args):
        if type(args[0]) == int:
            if type(args[0]) != int or type(args[1]) != int or (type(args[2]) != int and type(args[2]) != float):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            self.rows = args[0]
            self.cols = args[1]
            self.fill_value = args[2]

            self.matrix = [[self.fill_value for _ in range(self.cols)] for _ in range(self.rows)]
        else:
            for i in range(1, len(args[0])):
                if len(args[0][i]) != len(args[0][i - 1]):
                    raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            for i in args[0]:
                for j in i:
                    if type(j) != int and type(j) != float:
                        raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            self.rows = len(args[0])
            self.cols = len(args[0][0])
            self.matrix = args[0][:]

    def check(self, key):
        key1, key2 = key
        if type(key1) != int or type(key2) != int or not (0 <= key1 < self.rows) or not (0 <= key2 < self.cols):
            raise IndexError('недопустимые значения индексов')
        return True

    def __getitem__(self, key):
        self.check(key)
        r, c = key
        return self.matrix[r][c]

    def __setitem__(self, key, value):
        self.check(key)
        r, c = key
        if type(value) != int and type(value) != float:
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')
        self.matrix[r][c] = value

    def __add__(self, other):
        new = self.matrix[:]
        if not isinstance(other, Matrix):
            for i in range(len(new)):
                for j in range(len(new[i])):
                    new[i][j] += other
        else:
            if len(self.matrix) != len(other.matrix):
                raise ValueError('операции возможны только с матрицами равных размеров')
            for i in range(len(self.matrix)):
                if len(self.matrix[i]) != len(other.matrix[i]):
                    raise ValueError('операции возможны только с матрицами равных размеров')

            for i in range(len(new)):
                for j in range(len(new[i])):
                    new[i][j] += other.matrix[i][j]
        return new

    def __sub__(self, other):
        new = self.matrix[:]
        if not isinstance(other, Matrix):
            for i in range(self.cols):
                for j in range(self.rows):
                    new[i][j] -= other
        else:
            if len(self.matrix) != len(other.matrix):
                raise ValueError('операции возможны только с матрицами равных размеров')
            for i in range(len(self.matrix)):
                if len(self.matrix[i]) != len(other.matrix[i]):
                    raise ValueError('операции возможны только с матрицами равных размеров')

            for i in range(self.cols):
                for j in range(self.rows):
                    new[i][j] -= other.matrix[i][j]
        return new


lst2D = [[1, 2, 3], [4, 5, 6]]
mt = Matrix(lst2D)
matrix = Matrix(2, 3, 1)
matrix222 = mt + 10
print(matrix222)
matrix333 = mt + matrix
print(matrix333)
