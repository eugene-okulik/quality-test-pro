# Напишите функцию-генератор, которая генерирует список чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число
# 0, 1, 1, 2, 3, 5, 8, 13, 21

import sys

sys.set_int_max_str_digits(0)

my_count = [5, 200, 1000, 100000]
lastsymb = 100005
j = 0


def fibon(any_list, lasts):
    my_list = [0, 1]
    global j
    for i in range(0, lasts):
        fib = my_list[0] + my_list[1]
        my_list.append(fib)
        my_list.pop(0)
        if i + 3 == any_list[j]:
            yield fib
            j += 1
            if j > len(any_list) - 1:
                break


print("Выводим результат: ")
for fib in fibon(my_count, lastsymb):
    print("Число Фибоначчи c порядковым номером " + str(my_count[j]) + " является : " + str(fib))
