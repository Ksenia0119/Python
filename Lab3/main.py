__author__ = "Maltseva K.V."

# Задача 35б Даны действительные числа x, y, z. Вычислить:
# б) max2(x + y + z/2, xyz) + 1
# пояснение для пользователя
print("Даны действительные числа x, y, z. Вычислить:max^2(x + y + z/2, xyz) + 1 ")
# ввод чисел
print("Введите x")
x = float(input())
print("Введите y")
y = float(input())
print("Введите z")
z = float(input())
# вычисление по формуле
S = max( x + y + z/2, x*y*z) **2 + 1
# вывод результата
print(f"Результат = {S}")