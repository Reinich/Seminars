# Вывести элементы в обратном порядке

def rev_str(n):
    el = input()
    if n == 1:
        return el
    return rev_str(n - 1) + ' ' + el  # слева добавляем el, чтобы выводило в обратном порядке


m = int(input())
print(rev_str(m))
