import os
import json
import time

file_path = '/home/peter/projects/quality-test-pro/homework/eugene_okulik/example.txt'
# 'C:\home\peter\projects\quality-test-pro\homework\eugene_okulik\example.txt'
# 'C:\home\peter\projects\quality-test-pro\homework\eugene_okulik/example.txt'
my_path = os.path.dirname(os.path.dirname(__file__))
print(my_path)
path_to_file = os.path.join(my_path, 'example.txt')
print(path_to_file)


with open(path_to_file, 'a') as file:
    file.write('2')

time.sleep(15)


# file = open(path_to_file, 'w')
# file.write('UPD1111111slkdlskdjfsdlfkj111111111')
# print(json.load(file))
# file.close()
# time.sleep(15)

# file = open('data.txt')
# print(file.read())
# file.close()
