# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).
# # П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str str(self) -
# вызывается функциями str, print и format. Возвращает строковое представление объекта.

class Worker:

    def __init__(self, name, surname, pos, wage, bonus):
        self.name = name
        self.surname = surname
        self.pos = pos
        self.wage = wage
        self.bonus = bonus
        self._income = {'wage': self.wage, 'bonus': self.bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{sum(self._income.values())}'

    def __str__(self):
        return f'{self.name} {self.surname}, должность: {self.pos}, ЗП: {str(sum(self._income.values()))}'


obj = Position('Иван', 'Иванов', 'бухгалтер', 25000, 15000)
print(obj.get_full_name())
print(obj.get_total_income())
print(obj)