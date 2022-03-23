# Задача Codewars: 5 kyu
# given the first few terms of a sequence, can you figure out the formula that was used to generate these numbers, so we can find any term in the sequence?
#
# Task
# write a function that accepts an array of number(the first few terms of a sequence)
# your function should return a mapping function that accepts an integer(n) and then return the nth term of the sequence, where zero is the first term.
# in practice a sequance can be completed in many ways, assume that the equation used is a Polynomial, and find the simplest(smallest degree) equation possible, that leaves you with a single unique solution.


# Валидное решение на все тесты, кроме самого жесткого по скорости


# Функция поиска детерминанта матрицы
def determinant(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        answer = 0
        for i in range(width):
            m = [[matrix[j][k] for k in range(width) if (k != i)] for j in range(1, width)]
            sign *= -1
            answer = answer + mul * determinant(m, sign * matrix[0][i])
    return answer

# Функция поиска корней матрицы
def korni_func(lst, x, b):
    some_list = []
    for j in range(len(lst)):
        lst_x = list(map(list, lst))
        for i in range(len(lst)):
            lst_x[i][j] = b[i]
        some_list.append((determinant(lst_x, 1)) / x)
        # some_list.append((determinantOfMatrix(lst_x, 1)) / x)
    return some_list


def solve_sequence(seq):
    def solution(n):
        if len(seq) == 0:
            count = 0
        else:
            s = tuple(seq)
            k = len(s)

            # Разница значений исходного списка с первым
            b = tuple(s[i] - seq[0] for i in range(1, k))

            # Создаем матрицу
            lst = tuple([j ** (k - i) for i in range(1, k)] for j in range(1, k))

            # Ищем детерминант
            x = determinant(lst, 1)
            # x = determinantOfMatrix(lst, 1)

            # Ищем корни матрицы
            korni = korni_func(lst, x, b)

            # Ищем значение n-го члена списка
            n = 7
            count = 0
            for i in range(k - 1):
                count += (korni[i] * n ** (k - 1 - i))
            count += seq[0]

        return print(count)

    return solution


sequences = [
    ([2,4,6], [2,4,6,8,10,12,14,16,18,20]),
]
for initial_sequence, first_ten_terms in sequences:
    solution_function = solve_sequence(initial_sequence)
    solution_function(0)
