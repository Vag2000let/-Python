# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Toy:
    def __init__(self, type, name):
        self.type = type
        self.name = name


class Car(Toy):
    def form(self):
        print('Закупка сырья')

    def bodywork(self):
        print('Изготовление кузова')

    def color(self):
        print('Кузов машины окрашен')


my_car = Car('car', 'Skoda')

class Doll(Toy):
    def form(self):
        print('Закупка сырья')

    def bodywork(self):
        print('Изготовление')

    def packaging(self):
        print('Кукла упакована')


my_doll = Doll('Кукла', 'Barbie')


class Animals(Toy):
    def form(self):
        print('Закупка сырья')

    def bodywork(self):
        print('Изготовление')

    def color(self):
        print('Животное окрашено')

my_animal = Animals('животное', 'волк')


class ToyFactory:
    def __init__(self, my_animal, my_car, my_doll):
        super().__init__(Toy)
        self.my_animal = my_animal
        self.my_car = my_car
        self.my_doll = my_doll

    def create_toy(self):
        print('Cоздан экземпляр: ', self.type)


ToyFactory.create_toy(my_animal)

