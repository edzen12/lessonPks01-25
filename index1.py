class Transport:
    def __init__(self, speed,capacity):
        self._speed = speed #текущая скорость (км/ч)
        self._capacity = capacity #вместимость пассажиров
    
    def start(self): #сообщение, что транспорт начал движение
        pass

class Car(Transport):
    def __init__(self, speed, capacity, brand):
        super().__init__(speed, capacity)
        self.brand = brand # марка автомобиля
# stop() — выводит сообщение, что транспорт остановился.
# info() — возвращает строку с основной информацией о транспорте.
# Подкласс Car (наследует от Transport):
# Доп атрибуты: brand — марка автомобиля.
# Метод info() должен быть переопределён, чтобы добавлять информацию о марке.
# Подкласс Bus (наследует от Transport):
# Доп атрибут: route_number — номер маршрута.
# Метод info() также должен быть переопределён.
# Класс Electric:
# Имеет атрибут:
# _battery_level — уровень заряда батареи (%)
# Методы:
# charge() — заряжает батарею до 100%.
# battery_status() — показывает уровень заряда.
# Класс ElectricCar — пример множественного наследования:
# Наследуется от Car и Electric.
# Переопределяет метод info(), добавляя данные о заряде батареи.