# Пользователь вводит текст(строка). Словом считаетсяпоследовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 15

my_str = "She sells sea shells on the sea shore The shells " \
         "that she sells are sea shells I'm sure.So if she sells sea " \
         "shells on the sea shore I'm sure that the shells are sea "
print(set(my_str.split()))
print(f'{len(set(my_str.split()))}')
