__author__ = "Maltseva K.V."

from matrix_func import matrix_func_transpose
# Вызов функции с указанием всех параметров
matrix = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
result = matrix_func_transpose(matrix)
print(result)

# Вызов функции с указанием только конкретных параметров
matrix = [[1.1, 7.8], [7.8, 4.5]]
result = matrix_func_transpose(matrix=matrix)
print(result)

# Лямбда-функция для вычисления математического выражения
math_expression = lambda x, y: x*x+y

# Пример использования
result = math_expression(10, 5)
print(result)

# Вызов функции без параметров
#result = matrix_func_transpose()
#print(result)