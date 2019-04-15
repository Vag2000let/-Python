# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:
    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor


class Player(Person):
    def attack(self):
        self.armor = self.damage / self.armor  # Урон к броне
        print(self.armor)

    def count_health(self):
        self.health -= self.damage / self.armor  # Урон здоровью
        print(self.health)


user1 = Player(100, 60, 1.2)


class Enemy(Person):
    def attack(self):
        self.armor = self.damage / self.armor  # Урон к броне
        print(self.armor)

    def count_health(self):
        self.health -= self.damage / self.armor  # Урон здоровью
        print(self.health)


user2 = Enemy(150, 50, 1.2)

class Figth(Person):
    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2
        self.health = user1
        self.health = user2



    def fithting(self):
        while user1.health > 0 and user2.health > 0:
            user1.attack(user2)
            print('осталось здоровья: ', user1.health)

f = Figth
f.fithting()