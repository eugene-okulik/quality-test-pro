import os
import datetime

path_to_HWD = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
path_to_file = os.path.join('eugene_okulik', 'hw_11', 'data.txt')
path_to_file_1 = os.path.join(path_to_HWD, path_to_file)
print(path_to_file_1)


with open(path_to_file_1, 'r') as my_file:
    file_data = my_file.readlines()

for line in file_data:
    if line == file_data[0]:
        date_1 = f'{line.split()[1]} {line.split()[2]}'
    if line == file_data[1]:
        date_2 = f'{line.split()[1]} {line.split()[2]}'
    if line == file_data[2]:
        date_3 = f'{line.split()[1]} {line.split()[2]}'

# 2022-05-14 20:34:13.212967 - распечатать эту дату, но на три года позже. Должно получиться 2025-05-14 20:34:13.212967
date_1st = datetime.datetime.fromisoformat(date_1)
date_in_3y = date_1st + datetime.timedelta(days=1096)
print(date_in_3y)


# 2. 2023-07-15 18:25:10.121473 - распечатать какой это будет день недели
date_2nd = datetime.datetime.fromisoformat(date_2)
print(date_2nd.strftime('%A'))


# 3. 2023-06-12 15:23:45.312167 - распечатать сколько дней назад была эта дата
date_3rd = datetime.datetime.fromisoformat(date_3)
now = datetime.datetime.now()
days_ago = now - date_3rd
print(f'{days_ago.days} дней назад')
