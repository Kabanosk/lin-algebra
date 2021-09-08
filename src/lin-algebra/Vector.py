import random
import math as m


class Vector:

    def __init__(self, V: list):
        if type(V) != list:
            raise TypeError("Vector must have one-dimensional list as a parameter")
        if len(V) < 1:
            raise ValueError("Vector must include one or more numbers")
        if type(V[0]) != int and type(V[0]) != float:
            if type(V[0]) == list:
                raise ValueError("Vector must have one-dimensional list as a parameter")
            raise ValueError("Elements of the vector must be floats or integers")
        self.V = V

    def __add__(self, other):
        if type(other) != Vector:
            raise TypeError("You must change second parameter to Vector object")
        if len(self.size()) != len(other.size()):
            raise ValueError("You cannot add two vectors with different size")
        for i in range(self.size()):
            self.V[i] += other.V[i]
        return Vector(self.V)

    def __iadd__(self, other):
        if type(other) != Vector:
            raise TypeError("You must change second parameter to Vector object")
        if len(self.size()) != len(other.size()):
            raise ValueError("You cannot add two vectors with different size")
        for i in range(self.size()):
            self.V[i] += other.V[i]
        return Vector(self.V)

    def __sub__(self, other):
        if type(other) != Vector:
            raise TypeError("You must change second parameter to Vector object")
        if len(self.size()) != len(other.size()):
            raise ValueError("You cannot add two vectors with different size")
        for i in range(self.size()):
            self.V[i] -= other.V[i]
        return Vector(self.V)

    def __isub__(self, other):
        if type(other) != Vector:
            raise TypeError("You must change second parameter to Vector object")
        if len(self.size()) != len(other.size()):
            raise ValueError("You cannot add two vectors with different size")
        for i in range(self.size()):
            self.V[i] -= other.V[i]
        return Vector(self.V)

    def __mul__(self, n):
        if type(n) == int or type(n) == float:
            return self.vector_scalar_product(n)
        elif type(n) == Vector:
            return self.dot(n)
        else:
            raise TypeError("You must change second parameter to Matrix object or a number (float or int)")

    def __imul__(self, n):
        if type(n) == int or type(n) == float:
            return self.vector_scalar_product(n)
        elif type(n) == Vector:
            return self.dot(n)
        else:
            raise TypeError("You must change second parameter to Matrix object or a number (float or int)")

    def __eq__(self, other):
        if type(other) != Vector:
            return False
        elif self.V == other.V:
            return True
        return False

    def __ne__(self, other):
        if type(other) != Vector:
            return False
        elif self.V != other.V:
            return True
        return False

    def vector_scalar_product(self, scalar):
        if type(scalar) != int and type(scalar) != float:
            raise TypeError("You must change the parameter to number (float or int)")
        for i in range(self.size()):
            self.V[i] *= scalar
        return Vector(self.V)

    def dot(self, V1):
        if type(V1) != Vector:
            raise TypeError("You must change second parameter to Vector object")
        if self.size() != V1.size():
            raise ValueError("You cannot take the dot product from vectors with different sizes")
        sum_ = 0
        for i in range(self.size()):
            sum_ += self.V[i] * V1.V[i]
        return sum_

    def cross(self, V1):
        if type(V1) != Vector: raise TypeError("You must change second parameter to Vector object")
        if self.size() != 3 or V1.size() != 3:
            raise ValueError(
                "You cannot count cross product from this vectors (only 3-dimensional vectors are allowed)")
        else:
            result = Vector([self.V[1] * V1.V[2] - self.V[2] * V1.V[1],
                             self.V[2] * V1.V[0] - self.V[0] * V1.V[2],
                             self.V[0] * V1.V[1] - self.V[1] * V1.V[0]])
            return result, result.length()

    def size(self):
        return len(self.V)

    def length(self):
        sum_ = 0
        for i in self.V:
            sum_ += i ** 2
        return m.sqrt(sum_)

    def print(self):
        for i in self.V:
            print(f'| {i} |')

    def gen_zero(self, dimensions):
        tmp = []
        for _ in range(dimensions):
            tmp.append(0)
        return Vector(tmp)

    def gen_random(self, dimensions):
        tmp = []
        for _ in range(dimensions):
            tmp.append(random.random() * 30)
        return Vector(tmp)
