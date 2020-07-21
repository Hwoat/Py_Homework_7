'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку
конструктора класса (метод __init__()), который должен принимать
данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
Следующий шаг — реализовать перегрузку метода __str__() для
вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации
операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять
поэлементно — первый элемент первой строки первой
матрицы складываем с первым элементом первой строки
второй матрицы и т.д.
'''

##  Разные матрицы ##  Нагуглено_частично

from copy import deepcopy


class Matrix:
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):  # без аргументов
        return '\n'.join(['\t'.join(map(str, list)) for list in self.matrix])

    def __add__(self, other):
        return Matrix()

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

    def __add__(self, other):
        return Matrix(list(map(
            lambda x, y: list(map(lambda z, w: z + w, x, y)),
            self.matrix, other.matrix)))

    def __mul__(self, other):
        return Matrix([[i * other for i in list] for list in self.matrix])

    __rmul__ = __mul__
matrix_1 = [[5, 18, 11], [6, 17, 23], [41, 50, 9]]
matrix_2 = [[45, 8, 2], [6, 7, 93], [24, 5, 97]]

add_matrix_1 = Matrix(matrix_1)
add_matrix_2 = Matrix(matrix_2)

print(add_matrix_1.__add__(add_matrix_2))

matrix_3 = [[5, 18], [6, 17]]
matrix_4 = [[45, 8], [6, 7]]

add_matrix_3 = Matrix(matrix_3)
add_matrix_4 = Matrix(matrix_4)


print(add_matrix_3.__add__(add_matrix_4))