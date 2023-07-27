import statistics


class Flowers:

    def __init__(self, name, fresh, length, price):
        self.name = name
        self.fresh = fresh
        self.length = length
        self.price = price

    def __str__(self):
        return f'{self.name}: fresh {self.fresh}, length {self.length}, price {self.price}'

    def __repr__(self):
        return f'{self.name}: fresh {self.fresh}, length {self.length}, price {self.price}'


class Rosa(Flowers):
    color = 'red'


class Romashka(Flowers):
    color = 'white'


class Liliya(Flowers):
    color = 'yellow'


class Landysh(Flowers):
    color = 'White'


flower_1 = Rosa('Rosa', 15, 45, 50)
flower_2 = Romashka('Romashka', 20, 41, 9)
flower_3 = Liliya('Liliya', 3, 53, 63)
flower_4 = Landysh('Landysh', 6, 15, 99)


class Buket:

    def __init__(self, flowers):
        self.flowers = flowers

    def define_buket_age(self):
        list_of_ages = [flowers.fresh for flowers in self.flowers]
        buket_age = statistics.mean(list_of_ages)
        return buket_age

    def sort_by_length(self):
        return sorted(self.flowers, key=lambda flower: flower.length)

    def sort_by_price(self):
        return sorted(self.flowers, key=lambda flower: flower.price)

    @staticmethod
    def find_flower(price):
        for flower in buket_1.flowers:
            if price == flower.price:
                return flower.name


buket_1 = Buket(flowers=[flower_1, flower_2, flower_3, flower_4])

print(buket_1.define_buket_age())
print(buket_1.sort_by_length())
print(buket_1.sort_by_price())
print(buket_1.find_flower(9))
