"""classmethod в Python используется для создания методов, которые могут быть вызваны на классе, а не на экземпляре класса. Эти методы могут быть полезными, например, для создания фабричных методов, общих для всех экземпляров класса, а также для доступа к атрибутам класса без необходимости создавать экземпляр. Вот несколько примеров использования @classmethod:

Фабричные методы: classmethod может использоваться для создания экземпляров класса с определенными параметрами. Например:
python
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_child(cls, name):
        return cls(name, age=0)

child = Person.create_child("Alice")

class MyClass:
    instances = 0

    def __init__(self):
        MyClass.instances += 1

    @classmethod
    def get_instance_count(cls):
        return cls.instances

obj1 = MyClass()
obj2 = MyClass()
count = MyClass.get_instance_count()  # count равен 2
print(count)

class OneClass:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__init__()

    def __init__(self):
        self.value = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init_singleton()
        return cls._instance

    def init_singleton(self):
        self.value = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


if __name__ == "__main__":

    singleton_1 = Singleton()
    singleton_1.set_value("First instance")
    print(singleton_1.get_value())  # Вывод: "First instance"

    singleton_2 = Singleton()
    singleton_2.set_value("Second instance")
    print(singleton_1.get_value())  # Вывод: "Second instance"
    print(singleton_2.get_value())  # Вывод: "Second instance"

    print(singleton_1 is singleton_2)  # Вывод: True (Обе перемен

