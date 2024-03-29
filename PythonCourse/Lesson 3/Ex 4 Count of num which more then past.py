# Дан массив, состоящий из целых чисел. Напишите программу,
# которая подсчитает количество элементов массива, больших предыдущего
# (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2
# Пояснение: (-1 < 5, 2 < 3)

#1
list = [0, -1, 5, 2, 3]
count = 0
for i in range(1, len(list)):
    if list[i] > list[i - 1]:
        count += 1
print(count)

#2
list = [0, -1, 5, 2, 3]
print(len([list[i] for i in range(1, len(list)) if list[i] > list[i - 1]]))
