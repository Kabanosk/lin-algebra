import random
import math as m


class Matrix:

    def __init__(self, M):
        if type(M) != list and type(M[0]) != list:
            raise TypeError("Only two-dimensional list is allowed")
        else:
            self.M = M

    def __add__(self, other):
        if type(other) != Matrix:
            raise TypeError("You must change second parameter to Matrix object")
        M1 = other.M
        tmp = self.gen_zero(self.size()[0], self.size()[1]).M
        if not self.__is_equal(self.M, M1):
            raise ValueError("You cannot sum two matrices with a different number of rows or columns")
        for i in range(len(self.M)):
            for j in range(len(self.M[0])):
                tmp[i][j] = self.M[i][j] + M1[i][j]
        return Matrix(tmp)

    def __iadd__(self, other):
        if type(other) != Matrix:
            raise TypeError("You must change second parameter to Matrix object")
        M1 = other.M
        if not self.__is_equal(self.M, M1):
            raise ValueError("You cannot sum two matrices with a different number of rows or columns")
        for i in range(len(self.M)):
            for j in range(len(self.M[0])):
                self.M[i][j] += M1[i][j]
        return Matrix(self.M)

    def __sub__(self, other):
        if type(other) != Matrix:
            raise TypeError("You must change second parameter to Matrix object")
        M1 = other.M
        tmp = self.gen_zero(self.size()[0], self.size()[1]).M
        if not self.__is_equal(self.M, M1):
            raise ValueError("You cannot subtract two matrices with a different number of rows or columns")
        for i in range(len(self.M)):
            for j in range(len(self.M[0])):
                tmp[i][j] = self.M[i][j] - M1[i][j]
        return Matrix(self.M)

    def __isub__(self, other):
        if type(other) != Matrix:
            raise TypeError("You must change second parameter to Matrix object")
        M1 = other.M
        if not self.__is_equal(self.M, M1):
            raise ValueError("You cannot subtract two matrices with a different number of rows or columns")
        for i in range(len(self.M)):
            for j in range(len(self.M[0])):
                self.M[i][j] -= M1[i][j]
        return Matrix(self.M)

    def __eq__(self, other):
        if type(other) != Matrix:
            return False
        if self.M == other.M:
            return True
        return False

    def __ne__(self, other):
        if type(other) != Matrix:
            return False
        if self.M != other.M:
            return True
        return False

    def __mul__(self, M1):

        if type(M1) == float or type(M1) == int:
            tmp = self.gen_zero(self.size()[0], self.size()[1])
            for i in range(len(self.M)):
                for j in range(len(self.M[0])):
                    tmp = self.M[i][j] * M1
            return Matrix(tmp)
        elif type(M1) == Matrix:
            tmp = M1
            return self.__multiplication(tmp)
        else:
            raise TypeError("You must change second parameter to Matrix object or a number (float or int)")

    def __imul__(self, M1):
        if type(M1) == float or type(M1) == int:
            for i in range(len(self.M)):
                for j in range(len(self.M[0])):
                    self.M[i][j] *= M1
        elif type(M1) == Matrix:
            tmp1 = M1
            self.M = self.__multiplication(tmp1).M
        else:
            raise TypeError("You must change second parameter to Matrix object or a number (float or int)")
        return Matrix(self.M)

    @staticmethod
    def __is_equal(M1: list, M2: list):
        if len(M1) == len(M2) and len(M1[0]) == len(M2[0]):
            return True
        else:
            return False

    @staticmethod
    def __get_minor(M, i, j):
        return [row[:j] + row[j + 1:] for row in (M[:i] + M[i + 1:])]

    def __multiplication(self, M1):
        m_num_of_rows, m_num_of_columns = self.size()
        m1_num_of_rows, m1_num_of_columns = M1.size()
        result = self.gen_zero(m_num_of_rows, m1_num_of_columns).M
        if m_num_of_columns != m1_num_of_rows:
            raise ValueError("You cannot multiply this two matrices")
        for i in range(m_num_of_rows):
            for j in range(m1_num_of_columns):
                for k in range(m1_num_of_rows):
                    result[i][j] += self.M[i][k] * M1.M[k][j]
        return Matrix(result)

    def size(self):
        return len(self.M), len(self.M[0])

    def print(self):
        for row in self.M:
            print(row)

    def is_squared(self):
        if len(self.M) == len(self.M[0]):
            return True
        else:
            return False

    def det(self):
        if not self.is_squared():
            raise ValueError("You can only count determinant from square matrix")
        else:
            return self.__det(self.M.copy())

    def __det(self, M1):
        det = 0
        if len(M1) == 2:
            return M1[0][0] * M1[1][1] - M1[1][0] * M1[0][1]
        else:
            for i in range(len(M1)):
                tmp = []
                for j in range(1, len(M1)):
                    tmp_row = []
                    for k in range(len(M1)):
                        if k != i:
                            tmp_row.append(M1[j][k])
                    tmp.append(tmp_row)
                det += M1[0][i] * (-1) ** i * self.__det(tmp)
        return det

    def is_diagonal(self):
        if not self.is_squared():
            return False
        num_of_rows, num_of_columns = self.size()
        for i in range(num_of_rows):
            for j in range(num_of_columns):
                if i != j and self.M[i][j] != 0:
                    return False
                if i == j and self.M[i][j] == 0:
                    return False
        return True

    def get_main_diagonal(self):
        tmp = []
        num_of_columns = self.size()[1]
        for i in range(num_of_columns):
            tmp.append(self.M[i][i])
        return tmp

    def is_identity(self):
        if not self.is_squared():
            return False
        num_of_rows, num_of_columns = self.size()
        for i in range(num_of_rows):
            for j in range(num_of_columns):
                if i != j and self.M[i][j] != 0:
                    return False
                if i == j and self.M[i][j] != 1:
                    return False
        return True

    def is_antidiagonal(self):
        if not self.is_squared():
            return False
        num_of_rows, num_of_columns = self.size()
        for i in range(num_of_rows):
            for j in range(num_of_columns):
                if i != num_of_columns - j - 1 and self.M[i][j] != 0:
                    return False
                if i == num_of_columns - j - 1 and self.M[i][j] == 0:
                    return False
        return True

    def get_antidiagonal(self):
        tmp = []
        num_of_columns = self.size()[1]
        for i in range(num_of_columns - 1, -1, -1):
            tmp.append(self.M[num_of_columns - i][i])
        return tmp

    def is_exchange(self):
        if not self.is_squared():
            return False
        num_of_rows, num_of_columns = self.size()
        for i in range(num_of_rows):
            for j in range(num_of_columns):
                if i != num_of_columns - j - 1 and self.M[i][j] != 0:
                    return False
                if i == num_of_columns - j - 1 and self.M[i][j] != 1:
                    return False
        return True

    def trace(self):
        tab = self.get_main_diagonal()
        sum_ = 0
        for i in tab:
            sum_ += i
        return sum_

    def T(self):
        num_of_rows, num_of_columns = self.size()
        tmp1 = []
        for i in range(num_of_rows):
            tmp2 = []
            for j in range(num_of_columns):
                tmp2.append(self.M[j][i])
            tmp1.append(tmp2)
        return Matrix(tmp1)

    def inv(self):
        det = self.det()
        num_of_rows = self.size()[0]
        if num_of_rows == 2:
            return [[self.M[1][1] / det, -1 * self.M[0][1] / det],
                    [-1 * self.M[1][0] / det, self.M[0][0] / det]]
        cofactors = []
        for i in range(num_of_rows):
            cofactor_row = []
            for j in range(num_of_rows):
                minor = self.__get_minor(self.M, i, j)
                cofactor_row.append(((-1) ** (i + j)) * Matrix(minor).det())
            cofactors.append(cofactor_row)
        return Matrix(cofactors).T() * (1 / det)

    def gen_random(self, rows, columns):
        tmp = []
        for i in range(rows):
            tmp_row = []
            for j in range(columns):
                tmp_row.append(random.random() * 30)
            tmp.append(tmp_row)
        return Matrix(tmp)

    def gen_zero(self, rows, columns):
        return Matrix([[0 for x in range(columns)] for y in range(rows)])
