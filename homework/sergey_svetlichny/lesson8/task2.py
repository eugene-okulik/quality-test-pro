# Генераторы
# Дан такой кусок прайс листа:
#
# (Копируйте эту переменную (константу) в код прямо как есть)
#
# PRICE_LIST = '''тетрадь 50р
# книга 200р
# ручка 100р
# карандаш 70р
# альбом 120р
# пенал 300р
# рюкзак 500р'''
# При помощи генераторов превратите этот текст в словарь такого вида:
#
# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}
# Обратите внимание, что цены в словаре имеют тип int (они не в кавычках)


PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


# print(PRICE_LIST.splitlines()[0].split()[0])
# print(PRICE_LIST.splitlines()[0].split()[1])
# print(PRICE_LIST.splitlines()[0].rstrip((PRICE_LIST.splitlines()[0][-1])).split()[1])

# price_list_2 = PRICE_LIST.replace('0р', '0')

# print(PRICE_LIST.splitlines()[0].split()[1::2])  # list
# print(PRICE_LIST.splitlines()[0].split()[1::2].pop(0))  # element of list
# print(PRICE_LIST.splitlines()[0].split()[1::2].pop(0).rstrip(PRICE_LIST.splitlines()[0].split()[1::2].pop(0)[-1]))


# new_dict = {k: v for k, v in zip(PRICE_LIST.splitlines()[1].split()[0], PRICE_LIST.splitlines()[1].split()[1] )}
# new_dict = {k: v for k, v in zip(PRICE_LIST.split()[::2], PRICE_LIST.split()[1::2])}  # 50p - выводит список но с р.
# как сделать этот вывод без р?

# new_dict = {k: v for k, v in zip(PRICE_LIST.split()[::2], PRICE_LIST.split()[1::2].pop(0))}  # 5-разбивает 50р посимв.
# new_dict = {k: v for k, v in zip(PRICE_LIST.split()[::2], PRICE_LIST.split()[1::2][1])}  # берется цена второй строки

new_dict = {k: v for k, v in zip(PRICE_LIST.split()[::2], list(map(lambda x: int(x.rstrip(x[-1])),
                                                                   PRICE_LIST.split()[1::2])))}

# https://webdevblog.ru/kak-perebrat-slovar-v-python/
# https://medium.com/nerd-for-tech/python-substrings-everything-you-need-to-know-4cca526c07eb
# https://skillbox.ru/media/code/kak-udalit-element-iz-spiska-v-python/
# https://habr.com/ru/companies/piter/articles/674234/

# things = PRICE_LIST.split()[::2]
# prices = PRICE_LIST.split()[1::2]

# fixed_prices = list(map(lambda x: int(x.rstrip(x[-1])), prices))
# fixed_prices = list(map(lambda x: int(x.rstrip(x[-1])), PRICE_LIST.split()[1::2]))
# print(PRICE_LIST.splitlines()[0].rstrip((PRICE_LIST.splitlines()[0][-1])).split()[1])
# str = line.rstrip((line[-1]))

# print(things)
# print(fixed_prices)

print(new_dict)
