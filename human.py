# Класс Human
#
# 1. Создайте класс Human.
# 2. Определите для него два статических поля: default_name и default_age.
# 3. Создайте метод __init__(), который помимо self принимает еще два параметра: name и age. Для этих параметров задайте значения по умолчанию, используя свойства default_name и default_age. В методе __init__() определите четыре свойства: Публичные - name и age. Приватные - money и house.
# 4. Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.
# 5. Реализуйте справочный статический метод default_info(), который будет выводить статические поля default_name и default_age.
# 6. Реализуйте приватный метод make_deal(), который будет отвечать за техническую реализацию покупки дома: уменьшать количество денег на счету и присваивать ссылку на только что купленный дом. В качестве аргументов данный метод принимает объект дома и его цену.
# 7. Реализуйте метод earn_money(), увеличивающий значение свойства money.
# 8. Реализуйте метод buy_house(), который будет проверять, что у человека достаточно денег для покупки, и совершать сделку. Если денег слишком мало - нужно вывести предупреждение в консоль. Параметры метода: ссылка на дом и размер скидки
#
#
# Класс House
#
# 1. Создайте класс House
# 2. Создайте метод __init__() и определите внутри него два динамических свойства: _area и _price. 3. Свои начальные значения они получают из параметров метода __init__()
# 4. Создайте метод final_price(), который принимает в качестве параметра размер скидки и возвращает цену с учетом данной скидки.
#
#
# Класс SmallHouse
#
# 1. Создайте класс SmallHouse, унаследовав его функционал от класса House
# 2. Внутри класса SmallHouse переопределите метод __init__() так, чтобы он создавал объект с площадью 40м2
#
#
# Тесты
#
# 1. Вызовите справочный метод  default_info() для класса Human()
# 2. Создайте объект класса Human
# 3. Выведите справочную информацию о созданном объекте (вызовите метод info()).
# 4. Создайте объект класса SmallHouse
# 5. Попробуйте купить созданный дом, убедитесь в получении предупреждения.
# 6. Поправьте финансовое положение объекта - вызовите метод earn_money()
# 7. Снова попробуйте купить дом
# 8. Посмотрите, как изменилось состояние объекта класса Human




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