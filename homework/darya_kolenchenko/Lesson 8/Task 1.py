num_a = int(input('Enter number A: '))
num_b = int(input('Enter Number B: '))


def decorated_func(func):
    def wrapper(number_a, number_b):
        if number_a == number_b:
            result = func(number_a, number_b, action='+')
            return result
        elif number_a > number_b:
            result = func(number_a, number_b, action='-')
            return result
        elif number_a < number_b:
            result = func(number_a, number_b, action='/')
            return result
        elif number_a < 0 or number_b < 0:
            result = func(number_a, number_b, action='*')
            return result
    return wrapper


@decorated_func
def calc(number_a, number_b, action):
    if action == '+':
        result = number_a + number_b
    elif action == '-':
        result = number_a - number_b
    elif action == '/':
        result = number_a / number_b
    elif action == '*':
        result = number_a * number_b
    return result


print(calc(num_a, num_b))
