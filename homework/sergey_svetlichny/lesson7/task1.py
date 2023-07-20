# 9 july
import datetime

parsesymbols = [',', '.', '/', '-', ':']
date1 = ''
separ = ''
dategood = False


def inputdate():
    global date1
    date1 = input("А ну-ка введи-ка какую-нибудь дату: ")
    return date1


def parsedate():
    for symbol in parsesymbols:
        if date1.__contains__(symbol):
            global separ
            separ = symbol


def checklist():
    python_date = datetime.datetime.strptime(date1, '%d' + separ + '%m' + separ + '%Y')
    print('Данная дата в формате питона выглядит так: ')
    print(python_date)
    global dategood
    dategood = True


inputdate()
try:
    parsedate()
    checklist()
except ValueError:
    while not dategood:
        try:
            print('Ввести дату необходимо в формате: 31-12-2023')
            inputdate()
            parsedate()
            checklist()
        except ValueError:
            print("Неправильный формат даты")
