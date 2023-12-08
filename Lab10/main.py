_author_ = "Maltseva K.V."

from MyClass import MyClass
from ChildClass import ChildClass

# Создание экземпляров классов и добавление их в список
objects = []
objects.append(MyClass())
objects.append(ChildClass())
objects.append(ChildClass())
objects.append(MyClass())
objects.append(MyClass())

# Обработка списка в цикле
for obj in objects:
    obj.set_dictionary({"Иван": "3"})
    obj.set_my_list([1, 2, 3])
    print("Словарь:", obj.get_dictionary())
    print("Список:", obj.get_my_list())
    print("-" * 10)

# Удаление элементов списка
for obj in objects:
    del obj

# Проверка, что элементы были удалены
print(objects)