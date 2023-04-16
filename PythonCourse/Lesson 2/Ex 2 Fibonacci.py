a = int(input('Введите число: '))
f1, f2 = 1, 1
f = 0
n = 3  # индекс
while a > f2:
    n += 1
    f = f1 + f2
    f1, f2 = f2, f
print(n if a == f else '-1')



# num = int(input('Введите число: '))
# f1 = f2 = 1
# n = 3
# while num > f2:
#     f1, f2 = f2, f1 + f2
#     n += 1
# print(n if num == f2 else '-1')
