# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного.

def fill_list(x):
    list_a = []
    for _ in range(x):
        list_a.append(b := int(input(f'{_ + 1} эл-т: ')))
    print(list_a)
    return list_a


print(n := int(input('Введите количество эл-ов: ')))
list_n = fill_list(n)
count = 0

for i in range(1, n - 1):
    if list_n[i] > list_n[i - 1] and list_n[i] > list_n[i + 1]:
        count += 1

print(count)