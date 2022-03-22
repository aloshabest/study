# Задача Codewars: 5 kyu
# given the first few terms of a sequence, can you figure out the formula that was used to generate these numbers, so we can find any term in the sequence?
#
# Task
# write a function that accepts an array of number(the first few terms of a sequence)
# your function should return a mapping function that accepts an integer(n) and then return the nth term of the sequence, where zero is the first term.
# in practice a sequance can be completed in many ways, assume that the equation used is a Polynomial, and find the simplest(smallest degree) equation possible, that leaves you with a single unique solution.



# Валидное решение на все тесты, кроме самого жесткого


def determinant(matrix, mul):

    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        answer = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            answer = answer + mul * determinant(m, sign * matrix[0][i])
    return answer

seq = [5]
b = [seq[i]-seq[0] for i in range(1, len(seq))]

print(b)
ls = []
lst = []
for j in range(1, len(seq)):
    for i in range(1, len(seq)):
        ls.append(j**(len(seq)-i))
    lst.append(ls)
    ls = []
print(lst)

x = determinant(lst, 1)
print(x)

korni = []
for j in range(len(lst)):
    lst_x = list(map(list, lst))
    for i in range(len(lst)):
        lst_x[i][j] = b[i]
    korni.append((determinant(lst_x, 1)) / x)
print(korni)


n = 4
k = len(seq) - 1
count = 0
for i in range(k):
    count += (korni[i] * n ** (k - i))
count += seq[0]
print(int(count))


# def solve_sequence(seq):
#     def solution(n):
#         k = len(seq)
#         if len(seq) == 5:
#             for p in range(-10, 21):
#                 for q in range(-10, 21):
#                     for z in range(-10, 21):
#                         for v in range(-10, 21):
#                             if (p + q + z + v == seq[1] - seq[0]) and (
#                                     p * 16 + q * 8 + z * 4 + v * 2 == seq[2] - seq[0]) and \
#                                     (p * 81 + q * 27 + z * 9 + v * 3 == seq[3] - seq[0]) and (
#                                     p * 256 + q * 64 + z * 16 + v * 4 == seq[4] - seq[0]):
#                                     quest = [(p * n ** (k - 1)) + (q * n ** (k - 2)) + (z * n ** (k - 3)) + (v * n ** (k - 4)) + seq[0]]
#
#         elif len(seq) == 4:
#             for q in range(-10, 21):
#                 for z in range(-10, 21):
#                     for v in range(-10, 21):
#                         if (q + z + v == seq[1] - seq[0]) and (q * 8 + z * 4 + v * 2 == seq[2] - seq[0]) and (
#                                 q * 27 + z * 9 + v * 3 == seq[3] - seq[0]):
#                             quest = [(q * n ** (k - 1)) + (z * n ** (k - 2)) + (v * n ** (k - 3)) + seq[0]]
#
#         elif 1 < len(seq) < 4:
#             quest = [((seq[1] - seq[0]) * n) + seq[0]]
#
#         elif len(seq) == 1:
#             quest = [seq[0]]
#
#         elif len(seq) == 0:
#             quest = [0]
#
#         return quest[0]
#
#     return solution