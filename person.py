# Отдел кадров от нас требует хранить следующие персональные данные:
# ФИО;
# возраст (целое число от 14 до 120);
# серию и номер паспорта в формате xxxx xxxxxx, где x – цифра (от 0 до 9);
# вес, в кг (вещественное число от 20 и выше).


from string import ascii_letters


class Person:


    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()


    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)

        self.__fio = fio.split()
        self.old = old
        self.passport = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат записи ФИО")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("В ФИО должен быть хотя бы один символ")
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО можно использовать только буквенные символы и дефис")


    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("Возраст должен быть целым числом в диапазоне [14; 120]")


    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError("Вес должен быть вещественным числом от 20 и выше")


    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Паспорт должен быть строкой")

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный формат паспорта")

        for p in s:
            if not p.isdigit():
                raise TypeError("Серия и номер паспорта должны быть числами")


    @property
    def fio(self):
        return self.__fio


    @property
    def old(self):
        return self.__old


    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old


    @property
    def weight(self):
        return self.__weight


    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight


    @property
    def ps(self):
        return self.__ps


    @ps.setter
    def ps(self, ps):
        self.verify_ps(ps)
        self.__ps = ps



p = Person('Балакирев Сергей Михайлович', 20, '1234 567890', 80.0)
p.old = 100
p.passport = '4567 123456'
p.weight = 70.0
print(p.old)
print(p.__dict__)




print('-------------')
#
##
# Подключение дескрипторов
##
#
print('-------------')



class Verify:

    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат записи ФИО")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("В ФИО должен быть хотя бы один символ")
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО можно использовать только буквенные символы и дефис")


    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("Возраст должен быть целым числом в диапазоне [14; 120]")


    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError("Вес должен быть вещественным числом от 20 и выше")


    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Паспорт должен быть строкой")

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный формат паспорта")

        for p in s:
            if not p.isdigit():
                raise TypeError("Серия и номер паспорта должны быть числами")


    def __set_name__(self, owner, name):
        self.name = '_' + name


    def __get__(self, instance, owner):
        return getattr(instance, self.name)


    def __set__(self, instance, value):
        eval(f'self.verify' + self.name)(value)
        setattr(instance, self.name, value)


class Person2:

    fio = Verify()
    ps = Verify()
    weight = Verify()
    old = Verify()


    def __init__(self, fio, old, ps, weight):
        self.fio = fio
        self.old = old
        self.passport = ps
        self.weight = weight




p = Person2('Балакирев Дмитрий Владимирович', 50, '1234 567890', 50.0)
p.old = 90
p.passport = '4567 123456'
p.weight = 70.0
print(p.old)
print(p.__dict__)
