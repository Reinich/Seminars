# Напишите программу для печати всех уникальных значений в словаре.
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#          {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# список словарей
# my_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#            {"VI": "S005"}, {"VII": " S005 "}, {" V ": " S009 "}, {" VIII ": " S007 "}]

my_dict = {124: 's001',
           456: 's003',
           534: {124: 's002'}
           }
# for k, v in my_dict.items():  # возвращает и ключи, и значения
#     print(k, v)
# for v in my_dict.values():  # возвращает значение
#     print(v)
# for k in my_dict.keys():  # возвращает ключи
#     print(k)
# print(my_dict[534][124])  # копаем глубже в значения
# print(my_dict.get(534, '?'))  # получаение конкретного словаря или если его нет после запятой

dict_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
             {"VI": "S005"}, {"VII": " S005 "}, {" V ": " S009 "}, {" VIII ": " S007 "}]
all_val = set()
for into_dict in dict_list:
    val_set = set(into_dict.values())
    all_val |= val_set  # all_val.union(val_set)
# strip метод убирающий пробелы, работает в отдельном for как со строкой
print(all_val)

# print(*set([list(d.values())[0] for d in dict]))
