# Напишите программу, которая принимает на вхд строку, и отслеживает, сколько раз
# каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# a a a b c a a d c d d
# a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# .strip = убирает все пробелы справа и слева

# 1
word = 'a a a b c a a d c d d'
list_word = word.split(' ')
print(list_word)
i, n, word = 0, len(list_word), ''

while i < n:
    if list_word[:i].count(list_word[i]) == 0:
        word += f'{list_word[i]} '
    else:
        word += f'{list_word[i]}_{list_word[:i].count(list_word[i])} '
    i += 1
print(word)

# 2
s = ("a a a b c a a d c d d").split()
dict = {}
for i in s:
    if i not in dict:
        dict[i] = 0
        print(i, end=' ')
    elif i in dict:
        dict[i] += 1
        print(f'{i}_{dict[i]}', end=' ')
