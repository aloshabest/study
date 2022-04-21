# Напишите программу по следующему описанию. Есть класс "Воин". От него создаются два экземпляра-юнита.
# Каждому устанавливается здоровье в 100 очков. В случайном порядке они бьют друг друга.
# Тот, кто бьет, здоровья не теряет. У того, кого бьют, оно уменьшается на 20 очков от одного удара.
# После каждого удара надо выводить сообщение, какой юнит атаковал, и сколько у противника осталось здоровья.
# Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.


import random

class Warrior:
    count = 0

    def __init__(self, name, health=100):
        self.health = health
        self.name = name

    def strike(self, enemy):
        print(f"Раунд {self.count}")
        print(f'Воин {self.name} нанес урон -20 воину {enemy.name}, Здоровье воина {self.name} остается {self.health}')
        enemy.new_health(enemy.health - 20)
        print()

    def new_health(self, health):
        self.health = health
        print(f'Здоровье воина {self.name} уменьшилось до {self.health}')


def create_name():
    name = input('Введите имя воина ')
    return name

def create_health():
    while True:
        health = int(input('Введите здоровье воина '))
        if health > 0:
            return health
        print('Ваш воин изначально мертв, введите здоровье больше нуля ')


print("Создание первого воина")
first = Warrior(create_name(), create_health())
print("Создание второго воина")
second = Warrior(create_name(), create_health())


while (first.health > 0) and (second.health > 0):
    round = random.randint(1, 2)
    Warrior.count += 1

    if round == 1:
        name = first.name
        enemy_name = second.name
        first.strike(second)

    elif round == 2:
        name = second.name
        enemy_name = first.name
        second.strike(first)

print(f"Поздравляем воина {name}! Он одержал победу над воином {enemy_name}")