class User:  # отец

    def __init__(self, name):  # Перегрузка - когда мы меняем начинку
        self.name = name
        print(self.name)

    def func(self):
        pass


class Teacher(User):  # в принимаемом указываем отца, делая Teacher - наследником
    def __init__(self, name, surname):
        super().__init__(name)  # super - предок, указываем где брать name, НО только в дочернем __init__, если обращаться
        # к переменным в методе, достаточно просто self.name
        self.surname = surname

    def func(self):  # Переопределение - метод с одинаковыми именами имеет
        pass  # приоритет у наследника, поэтому он заменяется


# obj = Teacher('Ваня')
# print(obj.name)  # Ваня
obj = Teacher('Ваня', 'Иванов')
print(obj.surname)  # Ошибка, дается 3 аргумента, а должно 2, поэтому добавляем super().__init__(name)
