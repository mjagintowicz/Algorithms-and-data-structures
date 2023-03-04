#nieskonczone

from typing import Tuple


class Matrix:

    def __init__(self, size, p=0):
        if isinstance(size, Tuple):
            self.size = size
            m = []
            for r in range(size[0]):
                row = []
                for c in range(size[1]):
                    row.append(p)
                m.append(row)
            self.__m = m
        else:
            self.__m = size
            n_size = (len(size), len(size[0]))
            self.size = n_size

    def __add__(self, new_m):
        if self.size != new_m.size:
            raise ValueError("Incorrect size!")
        else:
            for row in range(new_m.size[0]):
                for col in range(new_m.size[1]):
                    new_m.__m[row][col] += self.__m[row][col]
        return new_m

    def __mul__(self, new_m):
        if self.size[1] != new_m.size[0]:
            raise ValueError("Incorrect size!")
        else:
            result = Matrix((self.size[0], new_m.size[1]))
            for row in range(result.size[0]):
                for col in range(result.size[1]):
                    sum = 0
                    for it in range(self.size[1]):
                        sum += self.__m[row][it] * new_m.__m[it][col]
                    result.__m[row][col] = sum
        return result

    def __getitem__(self, key):
        if key > self.size[0]:
            raise ValueError("Incorrect size!")
        return self.__m[key]

    def __str__(self):
        m_str = ""
        for row in self.__m:
            m_str += "|"
            for it in row:
                m_str += f' {it}'
            m_str += "| \n"
        return m_str


def power(x: int, n: int):
    result = 1
    for it in range(n):
        result *= x
    return result


def chio(matrix: Matrix, num=1):
    if matrix.size[0] != matrix.size[1]:
        raise ValueError("Incorrect size!")
    if matrix[0][0] == 0:
        for row in range(matrix.size[0]):
            if matrix[row][0] != 0:
                new_v = row
                break
        if 'new_v' not in locals():
            for col in range(matrix.size[1]):
                if matrix[0][col] != 0:
                    new_v = col
                    break
            if 'new_v' not in locals():
                    raise ValueError("TOO MANY ZEROS IN THE MATRIX")
            else:
                for elem in range(matrix.size[0]):
                    tmp = matrix[elem][new_v]
                    matrix[elem][new_v] = matrix[elem][0]
                    matrix[elem][0] = tmp
                    num *= -1
        else:
            for elem in range(matrix.size[0]):
                tmp = matrix[new_v][elem]
                matrix[new_v][elem] = matrix[0][elem]
                matrix[0][elem] = tmp
            num *= -1
    global det
    det = 1
    new_matrix = Matrix((matrix.size[0] - 1, matrix.size[1] - 1))
    num *= power(matrix[0][0], matrix.size[0] - 2)
    for r in range(new_matrix.size[0]):
        for c in range(new_matrix.size[1]):
            new_matrix[r][c] = matrix[0][0]*matrix[r+1][c+1] - matrix[r+1][0]*matrix[0][c+1]
    flag = True
    while flag:
        if new_matrix.size[0] == 1:
            flag = False
            det = new_matrix[0][0] / num
            break
        flag = False
        new_matrix, det = chio(new_matrix, num)
    return matrix, det


test_matrix = Matrix([
[5 , 1 , 1 , 2 , 3],

[4 , 2 , 1 , 7 , 3],

[2 , 1 , 2 , 4 , 7],

[9 , 1 , 0 , 7 , 0],

[1 , 4 , 7 , 2 , 2]

])
test_matrix_1 = Matrix([
     [0 , 1 , 1 , 2 , 3],
     [4 , 2 , 1 , 7 , 3],
     [2 , 1 , 2 , 4 , 7],
     [9 , 1 , 0 , 7 , 0],
     [1 , 4 , 7 , 2 , 2]
    ])


print("Wyznacznik macierzy 1: ", chio(test_matrix)[1])
print("Wyznacznik macierzy 2: ", chio(test_matrix_1)[1])
