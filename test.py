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

#test_matrix = [[1,1,1, 1],[16,8, 2, 4],[81,27, 3, 9],[256,64, 4, 16]]
test_matrix = [[1,1,1, 1],[16,8, 2, 4],[81,27, 3, 9],[256,64, 4, 16]]

print(determinant(test_matrix, 1))




def det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def minor(matrix, i, j):
    tmp = [row for k, row in enumerate(matrix) if k != i]
    tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
    return tmp


def determinant(matrix):
    size = len(matrix)
    if size == 2:
        return det2(matrix)

    return sum((-1) ** j * matrix[0][j] * determinant(minor(matrix, 0, j))
               for j in range(size))


m = [[2, 4, 1, 1],
     [0, 2, 1, 0],
     [2, 1, 1, 3],
     [4, 0, 2, 3]]

print(determinant(m))