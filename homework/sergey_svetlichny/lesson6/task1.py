# Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool. Спросите у пользователя salary.
# А bonus пусть назначается рандомом.
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
# Примеры результатов:
# 10000, True - '$10255'
# 25000, False - '$25000'
# 600, True - '$3785

from random import randint, choice

salary = int(input('Input your salary: '))
sumOfBonus = 0
bonus = choice((True, False))
if bonus:
    sumOfBonus = randint(int(salary * 0.05), int(salary * 0.2))  # ограничил диапазон бонуса от 5 до 20%
print(f"{salary}, {bonus} - ${salary + sumOfBonus} ")
