# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,
# dignissim vitae libero” и после этого выводит получившийся текст на экран.

text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,' \
       'dignissim vitae libero'
print("Text started:")
print(text)
my_list = text.split()
my_list_new = []
for i in range(0, len(my_list)):
    str1 = my_list[i]
    if my_list[i][-1] == ',':
        my_list_new.append(str1.rstrip(str1[-1]) + 'ing, ')
    elif my_list[i][-1] == '.':
        my_list_new.append(str1.rstrip(str1[-1]) + 'ing. ')
    elif str1.__contains__(','):
        str2 = str1.replace(',', "ing, ")
        my_list_new.append(str2 + 'ing ')
    else:
        my_list_new.append(my_list[i] + 'ing ')
text_new = ''
for i in range(0, len(my_list_new)):
    text_new += my_list_new[i]
print()
print("Text updated:")
print(text_new)
