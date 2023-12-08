__author__ = "Maltseva K.V."

from typing import List

# Транспонирование квадратной матрицы
def matrix_func_transpose(matrix: List[List[float]]) -> List[List[float]]:
    # Функция принимает матрицу из списка из списков чисел типа float.
    # Возвращает List[List[float]
    # Проверка входных данных
    assert isinstance(matrix, list), "Аргумент 'matrix' должен быть списком."
    assert all(isinstance(row, list) for row in matrix), "Матрица должна быть представлена списком списков."
    assert all(all(isinstance(element, float) for element in row) for row in
               matrix), "Элементы матрицы должны быть числами с плавающей точкой."
    assert len(matrix) == len(matrix[0]), "Матрица должна быть квадратной."

    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix