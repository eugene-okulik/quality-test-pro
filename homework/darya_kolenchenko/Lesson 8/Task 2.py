PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


list_from_string = PRICE_LIST.split()
list_keys = list(element for element in list_from_string[::2])
list_value = list(int(f'{element [:-1]}') for element in list_from_string if element.endswith('р'))
new_dict = dict(list(zip(list_keys, list_value)))
print(new_dict)
