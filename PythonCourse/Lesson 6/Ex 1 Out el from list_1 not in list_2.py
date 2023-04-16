# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке,
# в каком они идут в первом массиве), которых нет во втором массиве.

def fill_list(x):
    list_a = []
    for _ in range(x):
        list_a.append(b := int(input(f'{_ + 1} эл-т: ')))
    print(list_a)
    return list_a


print(n := int(input('Введите кол-во элементов первого массива: ')))
list_n = fill_list(n)
print(m := int(input('Введите кол-во элементов второго массива: ')))
list_m = fill_list(m)

for i in list_n:
    if i not in list_m:
        print(i, end=' ')
