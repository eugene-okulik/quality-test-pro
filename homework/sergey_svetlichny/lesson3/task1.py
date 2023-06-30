# 0
# Создайте словарь (и сохраните его в переменную my_dict) с такими ключами: ‘tuple’, ‘list’, ‘dict’, ‘set’.
# Для каждого элемента задайте значение соответствующее названию ключа. Например в элемент с ключом ‘tuple’ добавьте
# кортеж в качестве значения. Содержимое этого кортежа (или что вы там добавляете) - на вашу фантазию, но количество
# элементов в каждом таком значении должно быть не меньше пяти. Т.е. если добавляете кортеж, то в нем как минимум
# должно быть (1, 2, 3, 4, 5), если список, то не меньше пяти элементов, если словарь, то не меньше пяти пар
# ключ-значение, итд.
# Действия с элементами словаря my_dict:


my_dict = {'tuple': ("one", "two", "three", "four", "five"),
           'list': [1, 2, 3, 4, 5],
           'dict': {'odin': '1', 'dva': '2', 'tri': '3', 'chetyre': '4', 'pyat': '5'},
           'set': {"ein", "zwei", "drei", "vier", "funf"}}

print('my_dict:')
print(my_dict)
print('')

# 1
# Для того, что хранится под ключом ‘tuple’:
# выведите на экран последний элемент
print('task 1:')
tuple1 = my_dict.get('tuple')
print('tuple1:')
print(tuple1)
print('tuple1, last:')
print(tuple1[-1])
print('')

# 2
# Для того, что хранится под ключом ‘list’:
# добавьте в конец списка еще один элемент
# удалите второй элемент списка
print('task 2:')
list1 = my_dict.get('list')
print('list1:')
print(list1)
list1.append(6)
print('list1 with added:')
print(list1)
list1.pop(1)
print('list1 without removed:')
print(list1)
my_dict['list'] = list1
print('list in my_dict:')
print(my_dict.get('list'))
print('')

# 3
# Для того, что хранится под ключом ‘dict’:
# добавьте элемент с ключом ('i am a tuple',) и любым значением
# удалите какой-нибудь элемент
print('task 3:')
dict1 = my_dict.get('dict')
print('dict1:')
print(dict1)
dict1['(\'i am a tuple\',)'] = '(\'uno, due, tres\')'
print('dict1 updated:')
print(dict1)
my_dict['dict'] = dict1
print('dict in my_dict:')
print(my_dict.get('dict'))
print('')

# 4
# Для того, что хранится под ключом ‘set’:
# добавьте новый элемент в множество
# удалите элемент из множества
print('task 4:')
set1 = my_dict.get('set')
set1.add('sechs')
set1.remove('drei')
print('set1 updated:')
print(set1)
my_dict['set'] = set1
print('set in my_dict:')
print(my_dict.get('set'))
print('')

# 5
# В конце выведите на экран весь словарь

print("my_dict updated:")
print(my_dict)
