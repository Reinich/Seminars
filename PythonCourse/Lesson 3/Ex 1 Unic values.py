# Вытащить уникальные значения

#1 (через циклы)
list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
count = len(list_1)
for i in range(len(list_1) - 1):
    for j in range(i + 1, len(list_1)):
        count -= list_1[i] == list_1[j]
print(count)

#2 (через множества)
list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
sets = set()
for element in list_1:
    if element not in sets:
        sets.add(element)
print(len(sets))


#3 (через вхождение в список)
list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
count = 0
for i in range(len(list_1)):
  count += not list_1[i] in list_1[i + 1:]
print(count)