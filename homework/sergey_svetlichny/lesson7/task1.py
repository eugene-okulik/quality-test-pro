# 9 july
import datetime

parse_symbols = [',', '.', '/', '-', ':']


def input_date():
    inputted_date = input("А ну-ка введи-ка какую-нибудь дату: ")
    return inputted_date


def parsedate(date_to_parse):
    for symbol in parse_symbols:
        if date_to_parse.__contains__(symbol):
            return date_to_parse, symbol
    return


def checklist(date_separator_tuple):
    date = date_separator_tuple[0]
    separator = date_separator_tuple[1]
    python_date = datetime.datetime.strptime(date, '%d' + separator + '%m' + separator + '%Y')
    print('Данная дата в формате питона выглядит так: ')
    print(python_date)
    return True


while True:
    try:
        if checklist(parsedate(input_date())):
            break
    except ValueError:
        print('Ввести дату необходимо в формате: 31-12-2023')
    except TypeError:
        print('Не введен разделитель')
