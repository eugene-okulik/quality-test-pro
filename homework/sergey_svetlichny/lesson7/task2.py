# temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
# С помощью функции map создайте из этого списка новый список с жаркими днями. Будем считать жарким всё, что выше 28.
# Распечатайте из нового списка самую высокую температуру и самую низкую.

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

# решение через for:
# temp_list = []
# for x in temperatures:
#     if x > 28:
#         temp_list.append(x)

# решение через filter:
filtered = list(iter(filter(lambda x: x > 28, temperatures)))
print(filtered)
print(max(filtered))
print(min(filtered))

# неправильное решение через map 1:
# def find_high(list1):
#     temp_list = []
#     for x in list1:
#         if x > 28:
#             temp_list.append(x)
#     return temp_list
#
# new_list = list(map(find_high, temperatures))
# print(new_list)

# неправильное решение через map 2:
# def find_big(x):
#     if x > 28:
#         return x
#
# new_list = list(map(find_big, temperatures))
# print(new_list)

# неправильное решение через map 3 (используя лямбда):
# new_list = list(map(lambda x: x > 28, temperatures))
# print(new_list)
