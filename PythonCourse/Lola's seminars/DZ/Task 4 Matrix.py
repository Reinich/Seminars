# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать
# данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы. Пример матрицы: 3 на 2
# 31 22
# 37 43
# 51 86
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде. Далее реализовать перегрузку
# метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна
# быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
# матрицы складываем с первым элементом первой строки второй матрицы и т.д.
import random


class Matrix:
    def __init__(self, mx):
        matrix = []
        for el in mx:
            matrix.append([i for i in el])
        self.matrix = matrix

    def __str__(self):
        self.arr = '\n'.join(['\t'.join([str(j) for j in i])
                              for i in self.matrix])
        return self.arr

    def __add__(self, other):
        self.matrix = a
        self.other = b
        sum_matrix = a.copy()
        for i in range(len(a)):
            for j in range(len(a[i])):
                if len(a) == len(b) and len(a[i]) == len(b[i]):
                    sum_matrix[i][j] += b[i][j]
                else:
                    return 'Матрица разного размера. Сложить не получится.'
        return sum_matrix


a = [[31, 32], [37, 43], [51, 86]]
b = [[1, 2], [3, 4], [5, 6]]
obj = Matrix(a)
obj1 = Matrix(b)
print(obj)
sum_matr = obj + obj1
print(sum_matr)
