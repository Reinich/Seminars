class Car:
    # атрибуты класса
    wheels = 4
    rule = 1

    # методы класса
    def __init__(self, color, engine):  # self - это указание текущего класса,
        self.color = color  # поскольку здесь только инициализация объекта
        self.engine = engine

    def __add__(self, other):
        res = self.wheels + other.wheels
        obj_new = Car('red', 'gas')
        obj_new.wheels = res
        return obj_new

    def my_method(self):  # здесь self - это уже сам объект(переменная obj)
        res = self.wheels + self.rule
        return res

    def __str__(self):
        return 'объектус'


obj = Car()
obj = Car('red', 'gas')
print(obj.wheels)  # 4
obj.wheels = 5
print(obj.wheels)  # 5
print(obj.__dict__)  # {'color': 'red', 'engine': 'gas', 'wheels': 5}
print(Car.__dict__)  # {'wheels': 4, 'rule': 1} и прочие потроха
obj_1 = Car('blue', 'electric')
a = obj + obj_1
print(a.wheels)  # 9 - используется метод __add__
print(obj)  # объектус - используется метод __str__
