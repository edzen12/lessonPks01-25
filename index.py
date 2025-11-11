# Ввод и вывод (input() print())

# Типы данных
#     int 
#     float 
#     bool 
#     str 
#     list 
#     tuple
#     dict 
#     set frozenset 
#     None

# Переменные - хранить любой тип данных

# индексы 01234
# срезы [start:stop:step]

# Методы
    # str-строк .upper() .lower() .strip() .join()
    # list-списков .append() .pop() .remove() .insert()
    # dict-словарей .keys() .values() .items()
    # set-множеств .add() .remove() .discard .pop()

# операторы сравнения > < >= <= != ==
# ариф операторы + - * / ** // % += -= *= /=
# логические операторы and-и or-или not-не in-в
# Условные операторы if elif else 
# тернарный оператор

# Исключения try except

# цикл - повторение 
# for - для, while - пока  


# генератор списков - list comprehension

# модули
# работа с файлами r w a x b rb wb 

# функции
#     встроенные print() input() len() type()
#     пользовательские
#         lambda - анонимная функция, функция без имени
#         def - функция с именем и возможно с параметрами

# Это всё БАЗА

# ООП - объектно-ориентированное программирование
class Student: # 
    def __init__(self, name, age, group): # конструктор / магический метод инит
        self.name = name # атрибут класса
        self.__age = age # атрибут класса
        self._group = group # атрибут класса
    
    def info(self): # метод класса
        print(self.name, self.__age, self._group)

st = Student('GEna', 45, 'pks-01-25') # экземпляр класса
st.info() # Вызов метода класса