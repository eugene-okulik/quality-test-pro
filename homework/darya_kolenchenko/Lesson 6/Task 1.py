import random

salary = int(input('Enter salary: '))
define_bonus = random.choice([True, False])
end_bonus = round(random.random() * 1000)


def total_salary(oklad, zarplata, premia):
    if zarplata:
        print(f'{oklad}, {zarplata} - {oklad + premia}$')
    else:
        print(f'{oklad}, {zarplata} - {oklad}$')


print(total_salary(salary, define_bonus, end_bonus))
