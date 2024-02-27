"""`property` в Python - это специальный декоратор, который позволяет
определить методы для доступа, установки и удаления атрибута класса,
как если бы это были обычные атрибуты, но с дополнительной логикой.
Это позволяет инкапсулировать доступ к атрибутам и выполнить дополнительные "
       "действия при их доступе, установке и удалении. Вот примеры использования `property`:)

1. **Скрытие атрибута**:

"""
class Circle:
    def __init__(self, radius):
        self._radius = radius  # Приватный атрибут

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Радиус не может быть отрицательным")
        self._radius = value

circle = Circle(5)
print(circle.radius)  # Получаем радиус
circle.radius = 10  # Устанавливаем радиус


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(4, 5)
print(rect.area)  # Вычисляем площадь
print(rect.perimeter)  # Вычисляем периметр

class CachedProperty:
    def __init__(self, func):
        self.func = func
        self.value = None

    def __get__(self, instance, owner):
        if self.value is None:
            self.value = self.func(instance)
        return self.value

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @CachedProperty
    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area)  # Первый раз вычисляется и кэшируется
print(circle.area)  # Значение уже закэшировано

"""`property` полезен, когда необходимо контролировать доступ к атрибутам класса и 
добавить дополнительную логику при этом доступе, не нарушая интерфейса доступа к атрибутам.
"""

