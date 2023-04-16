# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его характеристику.

def same_by(f, vals):
    # res_vals = [f(i) for i in vals]
    # if len(set(res_vals)) <= 1:
    #     return True
    # return False
    # 2
    # if len(set(map(f, vals))) <= 1:
    #     return True
    # return False
    # 3
    # return True if len(set(map(f, vals))) <= 1 else False
    # 4
    return len(set(map(f, vals))) <= 1


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
