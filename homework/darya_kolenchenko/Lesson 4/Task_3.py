i = 0
while True:
    i += 1
    if i % 5 == 0 and i % 3 == 0:
        print('FuzzBuzz')
    elif i % 3 == 0:
        print('fuzz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
    if i > 99:
        break
