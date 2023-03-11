#skonczone

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


def transpose(matrix: Matrix) -> Matrix:
    t_size = tuple(reversed(matrix.size))
    t_matrix = Matrix(t_size)
    for row in range(matrix.size[0]):
        for col in range(matrix.size[1]):
            t_matrix[col][row] = matrix[row][col]
    return t_matrix


test_matrix = Matrix([[1, 0, 2], [-1, 3, 1]])
ones = Matrix((2, 3), 1)
test_matrix_1 = Matrix([[3, 1], [2, 1], [1, 0]])

print(transpose(test_matrix))
print(test_matrix + ones)
print(test_matrix * test_matrix_1)
