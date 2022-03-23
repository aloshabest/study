def getcofactor(m, i, j):
    return [row[: j] + row[j + 1:] for row in (m[: i] + m[i + 1:])]

def determinantOfMatrix(mat):

    if (len(mat) == 2):
        value = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
        return value
    Sum = 0
    for current_column in range(len(mat)):
        sign = (-1) ** (current_column)
        sub_det = determinantOfMatrix(getcofactor(mat, 0, current_column))
        Sum += (sign * mat[0][current_column] * sub_det)

    return Sum


mat = ([1],)

print('Determinant of the matrix is :', determinantOfMatrix(mat))





def determinantOfMatrix(mat, n):
    temp = [0] * n
    total = 1
    det = 1

    for i in range(0, n):
        index = i
        while (mat[index][i] == 0 and index < n):
            index += 1

        if (index == n):
            continue

        if (index != i):
            for j in range(0, n):
                mat[index][j], mat[i][j] = mat[i][j], mat[index][j]
            det = det * int(pow(-1, index - i))

        for j in range(0, n):
            temp[j] = mat[i][j]

        for j in range(i + 1, n):
            num1 = temp[i]
            num2 = mat[j][i]

            for k in range(0, n):
                mat[j][k] = (num1 * mat[j][k]) - (num2 * temp[k])
            total = total * num1

    for i in range(0, n):
        det = det * mat[i][i]

    return int(det / total)


mat = ([1],)
N = len(mat)
print(determinantOfMatrix(mat, N))





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






def det23(matrix):
    return matrix[0][0]*matrix[1][1]-matrix[1][0]*matrix[0][1]

# recursive part
def recursion(matrix, somme=None, prod=1):
    if(somme == None):
        somme = []
    if(len(matrix) == 1):
        somme.append(matrix[0][0])
    elif(len(matrix) == 2):
        somme.append(det23(matrix) * prod)
    else:
        for index, elmt in enumerate(matrix[0]):
            transposee = [list(a) for a in zip(*matrix[1:])]
            del transposee[index]
            mineur = [list(a) for a in zip(*transposee)]
            somme = recursion(mineur, somme, prod * matrix[0][index] * (-1)**(index+2))
    return somme

matrix = [[1]]

def main(matrix):
    return sum(recursion(matrix))
print(main(matrix))


def minor(matr, k):
    res = []
    for r in matr[1:]:
        row = []
        for j in range(len(r)):
            if j != k:
                row.append(r[j])
        res.append(row)
    return res

def det(matr):
    n = len(matr)
    if n == 2:
        return matr[0][0] * matr[1][1] - matr[0][1] * matr[1][0]
    s = 0
    z = 1
    for i in range(n):
        s = s + z * matr[0][i] * det(minor(matr, i))
        z = -z
    return s

m = [[1]]
print(det(m))






