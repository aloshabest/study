# Объявите класс GeyserClassic - фильтр для очистки воды. В этом классе должно быть три слота для фильтров. Каждый слот строго для своего класса фильтра:
#
# Mechanical - для очистки от крупных механических частиц;
# Aragon - для последующей очистки воды;
# Calcium - для обработки воды на третьем этапе.
#
# Объекты классов фильтров должны создаваться командами:
#
# filter_1 = Mechanical(дата установки)
# filter_2 = Aragon(дата установки)
# filter_3 = Calcium(дата установки)
# Во всех объектах этих классов должен формироваться локальный атрибут:
#
# date - дата установки фильтров (для простоты - положительное вещественное число).
#
# Также нужно запретить изменение этого атрибута после создания объектов этих классов (только чтение).
#
# Объекты класса GeyserClassic должны создаваться командой:
#
# g = GeyserClassic()
# А сам класс иметь атрибут:
#
# MAX_DATE_FILTER = 100 - максимальное время работы фильтра (любого)
#
# и следующие методы:
#
# add_filter(self, slot_num, filter) - добавление фильтра filter в указанный слот slot_num (номер слота: 1, 2 и 3), если он (слот) пустой (без фильтра).
# Также здесь следует проверять, что в первый слот можно установить только объекты класса Mechanical,
# во второй - объекты класса Aragon и в третий - объекты класса Calcium. Иначе, слот должен оставаться пустым.
#
# remove_filter(self, slot_num) - извлечение фильтра из указанного слота (slot_num: 1, 2, и 3);
#
# get_filters(self) - возвращает кортеж из набора трех фильтров в порядке их установки (по возрастанию номеров слотов);
#
# water_on(self) - включение воды: возвращает True, если вода течет и False - в противном случае.
#
# Метод water_on() должен возвращать значение True при выполнении следующих условий:
#
# - все три фильтра установлены в слотах;
# - все фильтры работают в пределах срока службы (значение (time.time() - date) должно быть в пределах [0; MAX_DATE_FILTER])



import time


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self, slot_1=None, slot_2=None, slot_3=None):
        self.slot = [slot_1, slot_2, slot_3]

    def add_filter(self, slot_num, filter):
        if slot_num == 1 and filter.name == Mechanical.name:
            if self.slot[0] is None:
                self.slot[0] = filter

        elif slot_num == 2 and filter.name == Aragon.name:
            if self.slot[1] is None:
                self.slot[1] = filter

        elif slot_num == 3 and filter.name == Calcium.name:
            if self.slot[2] is None:
                self.slot[2] = filter

    def remove_filter(self, slot_num):
        if slot_num == 1:
            self.slot[0] = None
        elif slot_num == 2:
            self.slot[1] = None
        elif slot_num == 3:
            self.slot[2] = None


    def get_filters(self):
        return self.slot[0], self.slot[1], self.slot[2]

    def water_on(self):
        if self.slot[0] != None and self.slot[1] != None and self.slot[2] != None:
            if 0 <= time.time() - self.slot[0].date <= GeyserClassic.MAX_DATE_FILTER and 0 <= time.time() - self.slot[1].date <= GeyserClassic.MAX_DATE_FILTER and 0 <= time.time() - self.slot[2].date <= GeyserClassic.MAX_DATE_FILTER:
                return True
        return False


class Mechanical:
    name = 'Mechanical'

    def __init__(self, date):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self):
        pass


class Aragon:
    name = 'Aragon'

    def __init__(self, date):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self):
        pass


class Calcium:
    name = 'Calcium'

    def __init__(self, date):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self):
        pass


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
print(my_water.slot)
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
print(my_water.slot)
print(w)
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() # True
print(my_water.slot)
print(w)
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно
print(my_water.slot)