from random import randrange, choice
from homework.eugene_okulik.utils import utils
from homework.eugene_okulik.utils import my_file_with_very_long_name as my_file

# print()
# input()
# int()

# print(random.random() * 100)
# print(random.randint(0, 5))
# print(random.randrange(0, 5))
# print(random.randrange(100, 1001, 10))
my_list = ['first', 'second', 'third']
# print(random.choice(my_list))
print(randrange(0, 5))
print(choice(my_list))

print(utils.a)
print(utils.calc(1, 2))
print(f'My string from imported file is {my_file.my_var}')

a = 1 / 3
print(round(a, 2))

b = -1

print(abs(b))

my_list2 = [2, 6, 1]
print(max(my_list2))
print(min(my_list2))
print(sum(my_list2))
print(sum(my_list2) / len(my_list2))


print(sorted(my_list2))
print(sorted(my_list2, reverse=True))
print(my_list2)
my_list2.sort()
my_list2.sort(reverse=True)
print(my_list2)

ttt = (1, 5, 2, 4)
print(sorted(ttt))
text = 'ksjdsyehdhd'
print(''.join(sorted(text)))
