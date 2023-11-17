__author__ = "Maltseva K.V."
# Задача 115в https://ivtipm.github.io/Programming/Glava04/index04.htm#z115
# пояснение для пользователя
print("Дано натуральное число n. Вычислить сумму от k=1 до n формулы 1/(2k+1)^2")
# ввод n
print("Введите n:")
n = int(input())
# счетчик цикла
k = 1
# накопление суммы
s = 0
# цикл пока k<=n
while k<=n:

    s = s + 1 / (2 * k + 1 ) ** 2
    k = k + 1
# вывод результата
print(f"Сумма {n} членов ряда = {s}")