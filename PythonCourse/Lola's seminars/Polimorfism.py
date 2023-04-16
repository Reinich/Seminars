class Auto:
    def auto_start(self, param_1, param_2=None):
        if param_2 is not None:
            print(param_1 + param_2)
        else:
            print(param_1)


class Bus:
    def auto_start(self, param_1, param_2=None):  # Два одинаковых метода,
        pass  # которые имеют разную суть, но один смысл: полиморфизм


a = Auto()
c = Bus()
lst = [a, c]  # lst = [Auto(), Bus()]

for el in lst:
    print(el.auto_start(1, 2))
