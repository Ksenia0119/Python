_author_ = "Maltseva K.V."
from MyClass import MyClass
# Класс наследуется от MyClass
class ChildClass(MyClass):
    # Конструктор
    def __init__(self):
        super().__init__()  # Вызов конструктора родительского класса

    # Дополнительная функция для ChildClass
    def additional_function(self):
        print("Некая дополнительная функция ChildClass")
    # Деструктор
    def __del__(self):
        for item in self.get_my_list():
            print("Удаленный элемент:", item)
        self.set_my_list([])  # Установка пустого списка