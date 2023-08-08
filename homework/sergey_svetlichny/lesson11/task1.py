# Нужно прочитать файлик, который лежит в моих папках. Здесь: \
#     quality_test_pro/homework/eugene_okulik/hw_11/data.txt
#
# Файлик не копируйте и никуда не переносите. Прочитайте его питоном, найдите в нём даты и сделайте с ними то, что после
# этих дат написано. Опирайтесь на то, что структура каждой строки одинакова: сначала идет номер, потом дата, потом
# дефис и после него текст

import os
import datetime

my_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
path_to_file = os.path.join(my_path, 'eugene_okulik', 'hw_11', 'data.txt')


def three_years_later(dat: datetime):
    years3 = 365 * 3
    new_date = dat + datetime.timedelta(years3)
    return new_date


def what_day_of_week(dat: datetime):
    return datetime.datetime.strftime(dat, '%A')


def days_ago(dat: datetime):
    now = datetime.datetime.now()
    days_ago = now - dat
    return days_ago.days


with open(path_to_file, "r", encoding="utf-8") as file:
    for line in file:
        line1 = line.split(' - ')
        what_to_do = line1[1].rstrip()
        date = line1[0].rstrip()[3::]
        my_date = datetime.datetime.fromisoformat(date)
        print('Дата:')
        print(date)
        print('Задание:')
        print(what_to_do)
        print('Мой ответ:')
        if what_to_do.__contains__('на три года позже'):
            print(three_years_later(my_date))
        elif what_to_do.__contains__('будет день недели'):
            print(what_day_of_week(my_date))
        elif what_to_do.__contains__('сколько дней назад'):
            print(days_ago(my_date))
        print()
file.close()
