class Human:

    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        return print(f"name - {self.name}, age - {self.age}, money - {self.__money}, house - {self.__house}")

    @staticmethod
    def default_info():
        return print(f"default_name - {Human.default_name}, default_age - {Human.default_age}")

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, mon):
        self.__money += mon
        print(f'Earned {mon} money! Current value: {self.__money}')

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print(f"Not enough money!")


class House:

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f'Final price: {final_price}')
        return final_price

class SmallHouse(House):

    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)





Human.default_info()

Alex = Human('Alex', 22)

Alex.info()

Small_house = SmallHouse(50000)

Alex.buy_house(Small_house, 10)

Alex.earn_money(100000)

Alex.info()

Alex.buy_house(Small_house, 10)

Alex.info()