def multiply(num_1, num_2):
    return num_1 * num_2


number_a = int(input('Enter number A: '))
number_b = int(input('Enter number B: '))


result1 = multiply(number_a, number_b)
if result1 <= 20:
    new_result = multiply(result1, 3)
else:
    new_result = multiply(result1, 2)
print(new_result)

multiply(number_a, number_b)
