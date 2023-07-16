my_dict = {'tuple': ('A', 'B', 1, 5, 'Secret', 'Shell'),
           'list': ['C', 'D', 2, 6, 'Shmicret', 'Smell'],
           'dict': {'day': '16', 'month': '08', 'year': '1901', 'city': 'New York', 'country': 'New York'},
           'set': {'E', 'F', 3, 7, 'Dreams', 'Motel'}}

print(my_dict['tuple'][-1])
my_dict['list'].append(10)
my_dict['list'].pop(3)
my_dict['dict'][('i am a tuple',)] = 'value for tuple'
my_dict['dict'].pop('month')
my_dict['set'].add('July')
my_dict['set'].pop()
print(my_dict)
