# Пользователь вводит два числа
# Программа умножает одно число на другое
# Если результат этого умножения больше 20, то этот результат умножается на 2. А если результат изначального умножения
# меньше или равно 20, то он умножается на 3

# print("Hello! Input please first digit")
a = int(input('Hello! Input please first digit '))
b = int(input('Input please second digit '))
# print("Input please second digit")
c = a * b
d = ''
if c > 20:
    d = c * 2
    print(f"{a} x {b} x 2 = ", end="")
elif c <= 20:
    d = c * 3
    print(f"{a} x {b} x 3 = ", end="")
print(d)
