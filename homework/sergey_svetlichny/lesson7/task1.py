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


def parsedate(date):
    for x in range(0, len(parsesymbols)):
        if date.__contains__(parsesymbols[x]):
            global separ
            separ = parsesymbols[x]
            my_list: list[str] = date1.split(parsesymbols[x])
            return my_list


def checklist(my_list, separ):
    python_date = datetime.datetime.strptime(date1, '%d' + separ + '%m' + separ + '%Y')
    print('Данная дата в формате питона выглядит так:: ')
    print(python_date)
    global dategood
    dategood = True


inputdate()
try:
    checklist(parsedate(date1), separ)
except ValueError:
    while not dategood:
        try:
            print('Ввести дату необходимо в формате: 31-12-2023')
            inputdate()
            checklist(parsedate(date1), separ)
        except ValueError:
            print("Неправильный формат даты")
