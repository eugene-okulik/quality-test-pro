# Этапы:
# 1. распознать аргументы, которые ввел пользователь
# 2. определить что указал пользователь: файл или папку
# 3. получить содержимое файла (файлов)
# 4. разбить содержимое на блоки и сохранить блоки в переменной
# 5. реализовать поиск по дате
# 6. реализовать поиск по тексту
# 7. настроить удобный вывод результатов

# здесь могли бы быть функции: data_to_dict, find_by_date, find_by_text, exclude_unwanted, print_result.
# Правильный алгоритм действий:
#
# Превращаем содержимое одного или всех файлов в словарь
# Если запрошен поиск по дате, оставляем в словаре только то, что соответствует поиску
# Если запрошен поиск по тексту, оставляем в словаре только то, что соответствует поиску
# Если указано unwanted, выбрасываем из словаря все, что имеет указанное слово
# Распечатываем весь словарь согласно тому, что просили (full или не full)

import argparse
import datetime
import os
import time
from os import walk

parsed_data = {}
inputted_date_analyzer = []
index_of_string_to_find = []
date_lines = []
parse_symbols = [',', '.', '/', '-', ':']
type_of_date = []  # not_date, good_d, less, more, range_d


def parse_separ(date_to_parse):
    for symbol in parse_symbols:
        if symbol in date_to_parse:
            return symbol
    return


def check_date_length(dat: str):
    if len(dat) == 20:
        if dat.endswith('+'):
            dat = dat[:19]
            return [check_inputted_date(dat), 'more']
        elif dat.endswith('-'):
            dat = dat[:19]
            return [check_inputted_date(dat), 'less']
    if len(dat) == 19:
        return [check_inputted_date(dat), 'date_ok']

    if len(dat) == 39:
        date1 = dat[0:19]
        date2 = dat[20:39]
        return [check_inputted_date(date1), 'range_d', check_inputted_date(date2)]

    if len(dat) == 11:
        if dat.endswith('+'):
            dat = dat[:10] + '-00-00-00'
            return [check_inputted_date(dat), 'more']
        elif dat.endswith('-'):
            dat = dat[:10] + '-00-00-00'
            return [check_inputted_date(dat), 'less']
    if len(dat) == 10:
        dat1 = dat + '-00-00-00'
        dat2 = dat + '-23-59-59'
        return [check_inputted_date(dat1), 'range_d', check_inputted_date(dat2)]


def check_inputted_date(dat):
    separator = parse_separ(dat)
    python_date = datetime.datetime.strptime(dat,
                                             f'%d{separator}%m{separator}%Y{separator}%H{separator}%M{separator}%S')
    return python_date


def data_to_dict(file_to_open):
    with open(file_to_open, "r", encoding="utf-8") as file:
        previous_date = ''
        my_str = ''
        my_counter = 0
        global date_lines
        for my_line in file:
            my_counter += 1
            time.sleep(0)
            list_of_words = my_line.split()
            first_word = list_of_words[0]
            if len(first_word) == 10 and '-' in first_word:
                date_lines.append(my_counter)
                python_date2 = datetime.datetime.strptime(my_line[:23], '%Y-%m-%d %H:%M:%S.%f')
                if args.full:
                    parsed_data.update({previous_date: my_str[47:]})
                    my_str = my_line.rstrip()
                    parsed_data[python_date2] = my_line[47:].rstrip()
                else:
                    parsed_data.update({previous_date: my_str[47:197]})
                    my_str = my_line[:300].rstrip()
                    parsed_data[python_date2] = my_line[47:300].rstrip()
                previous_date = python_date2
            else:
                if args.full:
                    my_str += my_line
        parsed_data.pop('', )


def find_all_indexes(input_str, search_str):
    length = len(input_str)
    index = 0
    l1 = []
    while index < length:
        i = input_str.find(search_str, index)
        if i == -1:
            return l1
        l1.append(i)
        index = i + 1
    return l1


def exclude_unwanted():
    for k, v in sorted(parsed_data.items()):
        if args.unwanted.lower in v.lower():
            parsed_data.pop(k)


def find_by_date():
    try:
        inputted_date = check_date_length(args.date)
        if inputted_date[1] == 'date_ok':
            for k, v in sorted(parsed_data.items()):
                if args.text is not None:
                    if (k.__format__('%Y-%m-%d %H:%M:%S') == inputted_date[0].__format__('%Y-%m-%d %H:%M:%S')
                            and args.text in v.lower()):
                        print(k, v)
                elif args.text is None:
                    if k.__format__('%Y-%m-%d %H:%M:%S') == inputted_date[0].__format__('%Y-%m-%d %H:%M:%S'):
                        print(k, v)

        if inputted_date[1] == 'more':
            for k, v in sorted(parsed_data.items()):
                if args.text is not None:
                    if k > inputted_date[0] and args.text in v.lower():
                        print(k, v)
                elif args.text is None:
                    if k > inputted_date[0]:
                        print(k, v)
        if inputted_date[1] == 'less':
            for k, v in sorted(parsed_data.items()):
                if args.text is not None:
                    if k < inputted_date[0] and args.text in v.lower():
                        print(k, v)
                elif args.text is None:
                    if k < inputted_date[0]:
                        print(k, v)
        if inputted_date[1] == 'range_d':
            if args.text is not None:
                for k, v in sorted(parsed_data.items()):
                    if inputted_date[0] < k < inputted_date[2] and args.text in v.lower():
                        print(k, v)
            elif args.text is None:
                for k, v in sorted(parsed_data.items()):
                    if inputted_date[0] < k < inputted_date[2]:
                        print(k, v)
    except ValueError:
        print('Ввести дату необходимо в формате: 31-12-2023-23-59-59')
        print('Разделитель должен быть один следующих: . , / - : ')
    except TypeError:
        print('Ввести дату необходимо cо временем, в формате: 31-12-2023-23-59-59')


def show_res_without_tex_without_date():
    for k, v in sorted(parsed_data.items()):
        print(k, v)


def find_by_text():
    for k, v in sorted(parsed_data.items()):
        lines = v.splitlines()
        counter = 0
        for line in lines:
            if args.text in line.lower():
                l2 = find_all_indexes(line.lower(), args.text)
                for lin in l2:
                    counter += 1
                    ind = lin
                    ind0 = ind - 150
                    ind1 = ind + 150
                    if ind0 < 0:
                        ind0 = 0
                    print(k, line[ind0:ind1])


isDirectory = False
parser = argparse.ArgumentParser()
parser.add_argument("file", help="Path to file or directory with logs")
parser.add_argument("-d", "--date", help="Date for search, format: 31-12-2022-23-59-59, "
                                         "31-12-2022-23-59-59- - to find earlier that this date and time, "
                                         "or 31-12-2022- - to find earlier that this day, "
                                         "31-12-2022-23-59-59+ - to find later that this date and time, "
                                         "or 31-12-2022+ - to find later that this start of this day, "
                                         "or 31-12-2022 - to find exactly in this day, "
                                         "30-12-2022-23-59-59-31-12-2022-23-59-59 - to find between these dates with "
                                         "time"
                                         "or 30-12-2022-31-12-2022 - to find between these dates")
parser.add_argument("-t", "--text", help="Text for search")
parser.add_argument("-n", "--unwanted", help="Text for except in results")
parser.add_argument("--full", help="Full text of logs", action="store_true")
args = parser.parse_args()

print(args)
print(args.file, args.date, args.text, args.unwanted, args.full)

fpath = args.file
isFile = os.path.isfile(args.file)
if not isFile:
    isDirectory = os.path.isdir(fpath)

if isDirectory:
    if args.text is not None:
        args.full = True
    filenames = next(walk(args.file), (None, None, []))[2]  # [] if no file
    for every_file in filenames:
        data_to_dict(os.path.join(args.file, every_file))

if isFile:
    data_to_dict(args.file)

if args.date is not None:
    find_by_date()

if args.unwanted is not None:
    exclude_unwanted()

if args.text is not None and args.date is None:
    args.text = args.text.lower()
    find_by_text()

elif args.date is None and args.text is None:
    show_res_without_tex_without_date()
