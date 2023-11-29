
import random
import copy
_author_ = "Maltseva K.V."

# https://ivtipm.github.io/Programming/Glava20/index20.htm#z678
# Задача 678 Дана действительная квадратная матрица, порядка n.
# Преобразовать матрицу по правилу: строку с номером n сделать столбцом с номером n,
# а столбец с номером n сделать строкой с номером n.

# пояснение пользователю
print("Дана действительная квадратная матрица, порядка n."
      " Преобразовать матрицу по правилу: строку с номером n сделать столбцом с номером n,"
      "а столбец с номером n сделать строкой с номером n.")

# Ввод размера матрицы с клавиатуры
n = int(input("Введите размер матрицы: "))

# Создание пустой матрицы
matrix = []

# Заполнение матрицы случайными значениями
for i in range(n):
    row = []
    for j in range(n):
        # Генерация случайного значения от 1 до 9
        value = random.randint(1, 9)
        row.append(value)
    matrix.append(row)

# Создание копии исходной матрицы
matrix_copy = copy.deepcopy(matrix)

# Вывод исходной матрицы
print("Исходная матрица:")
for row in matrix_copy:
    print(row)

# Преобразование матрицы
for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Вывод преобразованной матрицы
print("Преобразованная матрица:")
for row in matrix:
    print(row)