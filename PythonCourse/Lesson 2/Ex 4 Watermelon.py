count_wm = int(input('Введите количество арбузов: '))
min = int(input('Вес 1 арбуза: '))
max = min
min_i, max_i = 0, 0
for _ in range(1, count_wm):
    wm = int(input(f'Вес {_ + 1} арбуза: '))
    if wm > max:
        max = wm
        max_i = _
    if wm < min:
        min = wm
        min_i = _
print(f'Маленький арбуз весит {min}кг и стоит на {min_i + 1} месте, а большой арбуз весит {max}кг и стоит на {max_i + 1} месте')

