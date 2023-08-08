# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов. Создать экземпляры (объекты)
# цветов разных видов. Собрать букет (букет - еще один класс) с определением его стоимости. В букете цветы пусть
# хранятся в списке. Это будет список объектов.
#
# Для букета создать метод, который определяет время его увядания по
# среднему времени жизни всех цветов в букете.
#
# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)

# Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни) (и это тоже метод).

class Flower:
    def __init__(self, name, freshness, color, length, life_time_days, price):
        self.name = name
        self.freshness = freshness
        self.color = color
        self.length = length
        self.life_time_days = life_time_days
        self.price = price

    def __str__(self):
        return f'{self.name}, цена = {self.price} руб'

    # def __add__(self, obj):
    #     return self.price, obj.price


class Rose(Flower):

    def __init__(self, name, freshness, color, length, life_time_days, price, thorns_len):
        super().__init__(name, freshness, color, length, life_time_days, price)
        self.thorns_len = thorns_len


class Tulip(Flower):
    def __init__(self, name, freshness, color, length, life_time_days, price, tulip_size):
        super().__init__(name, freshness, color, length, life_time_days, price)
        self.tulip_size = tulip_size


class Astra(Flower):
    def __init__(self, name, freshness, color, length, life_time_days, price, diameter):
        super().__init__(name, freshness, color, length, life_time_days, price)
        self.diameter = diameter


class Bouquet:

    # def __init__(self, name, freshness, color, length, lifetimedays, price, flowers):
    def __init__(self, name, flowers):
        self.flowers = flowers
        self.name = name

    def __str__(self):
        return f', цена =  руб'

    def __livetime__(self):
        lt = 0
        for flower in self.flowers:
            lt += flower.life_time_days
        qty = len(self.flowers)
        avglt = round((lt / qty), 1)
        print('Примерное количество дней жизни букета = ', end='')
        return avglt

    def __search__(self, nam):
        print(f'ищем в букете название \'{nam}\' , результаты:')
        flws = []
        for flower in self.flowers:
            if flower.name.__contains__(nam):
                flws.append(flower.name)
        return flws

    def __cost__(self):
        summ = 0
        for flower in self.flowers:
            summ += flower.price
        print('Общая стоимость букета = ', end='')
        return summ

    def __gt__(self, obj):
        return self.price > obj.price

    def __ge__(self, obj):
        return self.price >= obj.price

    # def __lt__(self, obj):
    #     return self.price < obj.price
    #
    # def __le__(self, obj):
    #     return self.price <= obj.price
    def __sortir__(self):
        # max(self.flowers[0])
        print(sorted(self.flowers), self.flowers.flower.price)


flower_1 = Rose('Красная роза', 'fresh', 'red', '50cm', 7, 3, '0.5cm')
flower_2 = Astra('Белая астра', 'old', 'white', '30cm', 2, 1.5, '11cm')
flower_3 = Tulip('Желтый тюльпан', 'fresh', 'yellow', '35cm', 4, 2, 'big')
flower_4 = Rose('Кремовая роза', 'fresh', 'creme', '70cm', 8, 4, '0.3cm')
flower_5 = Astra('Красная астра', 'fresh', 'red', '40cm', 3, 1, '10cm')
flower_6 = Tulip('Королевский тюльпан', 'old', 'red', '30cm', 5, 2.5, 'big')
flower_7 = Rose('Белая роза', 'fresh', 'white', '60cm', 6, 5, '0.2cm')

# print(flower_1.price)
bouquet1 = Bouquet('Букет свадебный', [flower_1, flower_5, flower_7])

# print(flower_1 + flower_5)
# print(bouquet1.flowers[0])

print(bouquet1.__cost__())
print(bouquet1.__livetime__())
print(bouquet1.__search__('роза'))

print(flower_1 < flower_5)  # why there is an error?
print(bouquet1.__sortir__())
