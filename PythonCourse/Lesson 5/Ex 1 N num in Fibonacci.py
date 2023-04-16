# Найти N-ое число Фибоначчи

def fib(m):
    if m in [1, 2]:
        return 1
    return fib(m - 1) + fib(m - 2)


n = int(input('Введите место в Фибоначчи: '))
print(fib(n))
