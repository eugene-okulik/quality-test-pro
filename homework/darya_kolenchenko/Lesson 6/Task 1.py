import random

salary = int(input('Enter salary: '))
bonus = [True, False]
define_bonus = random.choice(bonus)
end_bonus = round(random.random() * 1000)


def total_salary(s, d, eb):
    if d:
        print(f'{s}, {d} - {s + eb}$')
    else:
        print(f'{s}, {d} - {eb}$')


print(total_salary(salary, define_bonus, end_bonus))
