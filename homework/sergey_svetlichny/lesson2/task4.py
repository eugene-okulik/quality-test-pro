import math

print("est' pryamougolnyi treugolnik")
a = int(input('vvedite katet a '))  # 3 and 5 , 9+25=34, c=6
b = int(input('vvedite katet b '))
print('gipotenuza c = ' + str(math.sqrt(a ** 2 + b ** 2)))
print("ploshchad' S = " + str(a * b / 2))
