_author_ = "Maltseva K.V."
# Класс
class MyClass:
    # Методы
    # Конструктор класса, инициализирует 2 поля - пустой словарь и пустой список
    def __init__(self):
        self._dictionary = {}
        self._my_list = []
    # Сеттер для установки нового значения словаря
    def set_dictionary(self, dictionary):
        assert isinstance(dictionary, dict), "Переданное значение не является словарем"
        self._dictionary = dictionary
    # Геттер для получения значения словаря
    def get_dictionary(self):
        return self._dictionary
    # Сеттер для установки нового значения списка
    def set_my_list(self, my_list):
        assert isinstance(my_list, list), "Переданное значение не является списком"
        self._my_list = my_list

    # Геттер для получения значения списка
    def get_my_list(self):
        return self._my_list
   # Деструктор, удаляет поочередно элементы из поля - списка
    def __del__(self):
        for item in self._my_list:
            print("Удаленный элемент:", item)
        self._my_list = []