# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,
# K – положительное число.

# 1
list = [1, 2, 3, 4]
print(list)
n, k = len(list), 6 % len(list) # чтобы можно было сдвинуть больше, чем размер листа

for i in range(k):
    num = list.pop(-1)
    list.insert(0, num)
print(list)

# 2
list_1 = [1, 2, 3, 4, 5]
k = 6 % len(list_1)

for i in range(k):
    num = list_1.pop(-1)
    list_1.insert(0, num)
print(list_1)

# 3
n = [1, 2, 3, 4, 5]

k = 5 % len(n)

new_list = n[k:] + n[:k]
print(new_list)
