# Хакер Василий)))))

# 1
journal = [1, 3, 3, 3, 4]
print(*journal)


def replace_grades(list_grades):
    min_num, max_num = min(list_grades), max(list_grades)
    for i in range(len(list_grades)):
        if list_grades[i] == max_num:
            list_grades[i] = min_num
    print(*list_grades)


replace_grades(journal)


# 2
journal = [1, 4, 3, 3, 4]
print(journal)


def del_all_max_value(arr):
    return ", ".join([str(i) for i in arr]).replace(str(max(arr)), str(min(arr)))


print(del_all_max_value(journal))