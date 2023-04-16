# Input: 6 -> -20 30 -40 50 10 -10 найти количество подряд положительный чисел
# Output: 2

# 1
num_days = int(input('Введите количество дней: '))
days_list = []
# range генератор список элементов, по одному
print('Введите температуру: ')
for i in range(1, num_days + 1):  # без счетчика, как и foreach
    day = int(input(f'{i}: '))
    days_list.append(day)  # добавляет элемент в список

temp_count, max_count = 0, 0
for temp in days_list:
    if temp > 0:
        temp_count += 1
    else:
        temp_count = 0
    if temp_count > max_count:
        max_count = temp_count

print(max_count)

# 2
num_days = int(input('Введите количество дней: '))
temp_count, max_count = 0, 0

print('Введите температуру: ')
for i in range(1, num_days + 1):
    temp = int(input(f'{i} день: '))
    if temp > 0:
        temp_count += 1
    else:
        temp_count = 0
    if temp_count > max_count:
        max_count = temp_count
print(max_count)
