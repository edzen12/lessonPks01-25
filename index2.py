class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}")

class Employee(Person):
    def __init__(self, name, age, salary, position):
        super().__init__(name, age)
        self.salary = salary # зарплата
        self.position = position # должность
    
    def calculate_salary(self): # 
        return self.salary

    def info(self):
        person = super().info()
        print(f"{person}, Имя: {self.name}, Возраст: {self.age}, Должность: {self.position}, Зарплата: {self.salary}")

class Chef(Employee): #повар
    def cook(self, dish_name):
        print(f"Повар {self.name} готовит {dish_name}")

class Waiter(Employee): #официант
    def take_order(self, dish_names, menu):
        order = Order()
        for name in dish_names:
            dish = menu.find_dish(name)
            if dish:
                order.add_dish(dish)
            else:
                print(f"Блюдо {name} отсутствует в меню")
        print(f"Официант {self.name} принял заказ: {[d.name for d in order.dishes]}")
        return order 
    
class Manager(Employee):  # менеджер.
    def calculate_profit(self, income, expenses):  # income-доходы, expenses-расходы
        profit = income-expenses
        print(f"Менеджер {self.name} подсчитал прибыль {profit} сом")
        return profit

class Dish:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
    def  __str__(self):
        return f"Блюдо: {self.name}, Цена: {self.price}, Ингредиенты: {', '.join(self.ingredients)}"

class Menu:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)
        print(f"Добавлено в меню: {dish}")

    def remove_dish(self, name):
        self.dishes.remove(name)
        print(f"Удалено в меню: {name}") 

    def find_dish(self, name):
        for dish in self.dishes:
            if dish.name == name:
                return dish 
        return None 

    def show_menu(self):
        print("Меню ресторана: ")
        for dish in self.dishes:
            print(f".   {dish}")
        print('----------')

class Order: # Заказ
    def __init__(self):
         self.dishes = []
         self.total = 0
         self.is_paid = False
    
    def add_dish(self, dish):
        self.dishes.append(dish)
    
    def calculate_total(self): #суммирует цены блюд
        self.total = sum(d.price for d in self.dishes)
        print(f"Общая сумма заказа {self.total}сом")
        return self.total

    def pay(self): #устанавливает is_paid = True и печатает чек
        self.is_paid = True
        print(f"Заказ оплачен. Спасибо за покупку")
        print('Чек: ')
        for dish in self.dishes:
            print(f" - {dish.name}: {dish.price}")
        print(f"Итого {self.total}сом")

 
class Restaurant:
    def __init__(self,name, menu):
        self.name = name
        self.menu = menu
        self.employees = []
        self.orders = []
        
    def add_employee(self, employee):
        pass

    def add_order(self, order):
        pass

    def show_employees(self):
        pass

    def show_orders(self):
        pass
    def total_income(self):
        pass