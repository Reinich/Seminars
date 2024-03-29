# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода. Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    MASS = 25
    THICKNESS = 0.05

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_asphalt(self):
        mass = self._length * self._width * Road.MASS * Road.THICKNESS
        return mass


obj = Road(20, 5000)
print(obj.mass_asphalt())
