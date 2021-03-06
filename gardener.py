# Класс Tomato:
# Создайте класс Tomato
# Создайте статическое свойство states, которое будет содержать все стадии созревания помидора
# Создайте метод __init__(), внутри которого будут определены два динамических protected свойства: 1) _index - передается параметром и 2) _state - принимает первое значение из словаря states
# Создайте метод grow(), который будет переводить томат на следующую стадию созревания
# Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)
#
# Класс TomatoBush
# Создайте класс TomatoBush
# Определите метод __init__(), который будет принимать в качестве параметра количество томатов и на его основе будет создавать список объектов класса Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап созревания
# Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
# Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая
#
# Класс Gardener
# Создайте класс Gardener
# Создайте метод __init__(), внутри которого будут определены два динамических свойства: 1) name - передается параметром, является публичным и 2) _plant - принимает объект класса Tomato, является protected
# Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым
# Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай. Если нет - метод печатает предупреждение.
# Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству.
#
# Тесты:
# Вызовите справку по садоводству
# Создайте объекты классов TomatoBush и Gardener
# Используя объект класса Gardener, поухаживайте за кустом с помидорами
# Попробуйте собрать урожай
# Если томаты еще не дозрели, продолжайте ухаживать за ними
# Соберите урожай
#

class Tomato:

    states = [0, 1, 2, 3, 4, 5]
    n = 0

    def __init__(self, index):
        self._index = index
        self._state = self.n

    def grow(self):
        if self.n < (len(self.states) - 1):
            self.n += 1

    def is_ripe(self):
        if self.n == (len(self.states) - 1):
            return True
        else:
            return False


class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []

class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Gardener is working...')
        self._plant.grow_all()
        print('Gardener finished')

    def harvest(self):
        print('Gardener is harvesting...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Harvesting is finished')
        else:
            print('Too early! Your plant is green and not ripe.')

    @staticmethod
    def knowledge_base():
        print("Harvest time for tomatoes should ideally occur\nwhen the fruit is a mature green and then allowed to ripen off the vine.\nThis prevents splitting or bruisingand allows for\na measure of control over the ripening process.")

Gardener.knowledge_base()

great_tomato_bush = TomatoBush(4)

gardener = Gardener('Emilio', great_tomato_bush)

gardener.work()

gardener.work()

gardener.harvest()

gardener.work()

gardener.harvest()







