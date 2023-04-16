import math
n = int(input('Введите число N: '))
s = 1
while n > 0:
    s *= n
    n -= 1

print(f'N! = {s}')



