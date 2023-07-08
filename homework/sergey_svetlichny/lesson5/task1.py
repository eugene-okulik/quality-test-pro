# Пользователь вводит два числа
# Программа умножает одно число на другое
# Если результат этого умножения больше 20, то этот результат умножается на 2. А если результат изначального умножения
# меньше или равно 20, то он умножается на 3

# print("Hello! Input please first digit")
a = int(input('Hello! Input please first digit '))
b = int(input('Input please second digit '))


def multipl(x, y):
    z = x * y
    return (z)


c = multipl(a, b)
d = ''
e = 2
znak = '>'
if c <= 20:
    e = 3
    znak = '<='
d = multipl(c, e)
print(f"{c} {znak} 20, so multiply on {e} ")
print(f"{a} x {b} x {e} = ", end="")
print(d)
