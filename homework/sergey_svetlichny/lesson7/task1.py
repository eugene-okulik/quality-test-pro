import datetime

parse_symbols = [',', '.', '/', '-', ':']


def input_date():
    inputted_date = input("А ну-ка введи-ка какую-нибудь дату: ")
    return inputted_date


def parse_separ(date_to_parse):
    for symbol in parse_symbols:
        if date_to_parse.__contains__(symbol):
            # return date_to_parse, symbol
            return symbol
    return


# def checklist(date_separator_tuple):
#     date = date_separator_tuple[0]
#     separator = date_separator_tuple[1]
#     python_date = datetime.datetime.strptime(date, '%d' + separator + '%m' + separator + '%Y')

def checklist():
    date = input_date()
    separator = parse_separ(date)
    python_date = datetime.datetime.strptime(date, f'%d{separator}%m{separator}%Y')
    print('Данная дата в формате питона выглядит так: ')
    print(python_date)
    return True


while True:
    try:
        # if checklist(parsedate(input_date())):
        if checklist():
            break
    except ValueError:
        print('Ввести дату необходимо в формате: 31-12-2023')
        print('Разделитель должен быть один следующих: . , / - : ')
    except TypeError:
        print('Не введен разделитель, разделитель должен быть один следующих: . , / - : ')
