# Декораторы добавляют функциональность в существующий код
# Декоратор - это паттерн программирования, который позволяет добавлять НОВЫЙ ФУНКЦИОНАЛ к существующей функции

def gre():
    print("Привет")

hello = gre  # функция - это объект
hello()

# №№№№№№№№№№№№№

def gromko(text):
    return text.upper()

def tiho(text):
    return text.lower()

def speak(func):
    message = func('Hello Pks-01-25')
    print(message)

speak(gromko)
speak(tiho)


####

def inc(x):
    return x*2

def dec(x):
    return x/2

def oper(func, x):
    res = func(x)
    return res 

print(oper(inc, 3))
print(oper(dec, 4))


#####


def before_after(func):
    def wrapper():
        print("перед вызовом функции")
        func()
        print("после вызова функции")
    return wrapper

@before_after #декоратор
def sayHey():
    print('Привет друг')

sayHey()

#########
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} c аргументами {args} {kwargs}")
        res = func(*args, **kwargs)
        print(f"Результат: {res}")
        return res
    return wrapper

@logger
def add(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

add(4,5,6,7,8)
add(56,77,n = 5, g=7)
add(n = 5, g=7)


###########
# @property - это встроенный декоратор 
#     getter - получение
#     setter - изменение
#     deleter - удаление
# Позволяет нам обращаться к методу как к полю атрибута

# без @property
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    def get_area(self):
        return 3.14 * self._radius ** 2
    
c = Circle(5)
print(c.get_area())
###
# 
class Person:
    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        print('Сеттер сработал')
        if not isinstance(value, str):
            raise ValueError('имя должно быть строкой')
        self.__name = value
    @name.deleter
    def name(self):
        print("Делетер сработал")
        del self.__name
    
p = Person('Gena')
p.name = 'Alex'
print(p.name)
del p.name
########
