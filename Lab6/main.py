import random as r
_author_ = "Maltseva K.V."

# Задача 136ж  https://ivtipm.github.io/Programming/Glava06/index06.htm#z136

# пояснение пользователю
print("Даны натуральное число n, действительные числа a1,..., an. Вычислить: ж) a1 - a2 + a3 - ... + (-1)^(n+1)an")
# ввод чисел
print("Введите n:")
# n = введенному числу с клавиатуры
n = int(input())
# заполняем массив рандомными числами от 1 до n включительно
# arr = [1,0,1,4,78,10]
arr = [r.randint(1, 100) for i in range(1, n+1)]
# arr = [i for i in range(1,n+1)]
# переменная для суммирования
total = 0
# проходимся по каждому элементу массива
for num in arr:
    # если элемент кратен 2
    if arr.index(num) % 2 == 0:
        # суммируем
        total += num
    # иначе
    else:
        # вычитаем
        total -= num
# выводим результат
print("Массив имеет следующий вид: ")
print(arr)
print(f"Значение выражения = {total}")
