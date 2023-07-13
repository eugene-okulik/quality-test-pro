def fib(n):
    num_a, num_b = 0, 1
    for number in range(n):
        yield num_a
        num_a, num_b = num_b, num_a + num_b


gen = list(fib(100001))
print(gen[5], gen[200], gen[1000], gen[100000])


# print("%e" % gen[5], "%e" % gen[200], "%e" % gen[1000], "%e" % gen[100000])
# бьет ошибку, форматирование не может обработать последнее число
