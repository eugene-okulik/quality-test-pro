# Задание на декораторы
# Напишите программу: Есть функция которая делает одну из арифметических операций с переданными ей числами (числа и
# операция передаются в аргументы функции). Функция выглядит примерно так:
#
# def calc(first, second, operation):
#     if operation == '+':
#     .....
# Программа спрашивает у пользователя 2 числа (вне функции)
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
# 1 если числа равны, то функция calc вызывается с операцией сложения этих чисел
# 3 если первое больше второго, то происходит вычитание второго из первого
# 4 если второе больше первого - деление первого на второе
# 2 если одно из чисел отрицательное - умножение


# решение через 2 функции:
# def wrapper(first, second):
#     if a == b:
#         print("Числа равны, поэтому мы их складываем")
#         return "+"
#     elif (a < 0) or (b < 0):
#         print("Есть отрицательное число, поэтому мы умножаем")
#         return "*"
#     elif a > b:
#         print("Первое число больше второго, поэтому делаем вычитание")
#         return "-"
#     elif b > a:
#         print("Второе число меньше первого, поэтому делаем деление")
#         return "/"
#
#
#
#
# def calc(first, second, operation):
#     if operation == '+':
#         return first + second
#     elif operation == '*':
#         return first * second
#     elif operation == '-':
#         return second - first
#     elif operation == '/':
#         return first / second
#


# a=int(input('Введите первое число: '))
# b=int(input('Введите второе число: '))
# print(calc(a,b, wrapper(a,b)))


# решение через декоратор:
def find_operator(func):
    def wrapper(a, b):
        if a == b:
            print("Числа равны, поэтому мы их складываем")
            func(a, b, '+')
        elif (a < 0) or (b < 0):
            print("Есть отрицательное число, поэтому мы умножаем")
            func(a, b, '*')
        elif a > b:
            print("Первое число больше второго, поэтому делаем вычитание")
            func(a, b, '-')
        elif b > a:
            print("Второе число меньше первого, поэтому делаем деление")
            func(a, b, '/')

    return wrapper


@find_operator
def calcul(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '*':
        return first * second
    elif operation == '-':
        return second - first
    elif operation == '/':
        return first / second


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(calcul(a, b))
