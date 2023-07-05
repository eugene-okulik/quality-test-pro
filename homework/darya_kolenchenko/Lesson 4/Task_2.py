
k = 14
while True:
    p = int(input('Угадай цифру: '))
    if p == k:
        print('Поздравляю! Вы угадали!')
        break
    elif p != k:
        print('Попробуйте снова')

