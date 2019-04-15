# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class TownCar:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = False

    def go(self):
        print(self.name, self.color, 'поехала со скоростью', self.speed)

    def turn(self):
        print(self.name, self.color, 'повернул на право', self.is_police)

    def stop(self):
        print(self.name, self.color, 'остановилась', self.is_police)


car = TownCar('Mersedes E200', 'синий', '120', 'is_police')


class SportCar:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = False

    def go(self):
        print(self.name, self.color, 'поехала со скоростью', self.speed, self.is_police)

    def turn(self):
        print(self.name, self.color, 'повернул на право', self.is_police)

    def stop(self):
        print(self.name, self.color, 'остановилась', self.is_police)


car1 = SportCar('Ferrari', 'красный', '250', 'is_police')

#car1.stop()

class WorkCar:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = False

    def go(self):
        print(self.name, self.color, 'поехала со скоростью', self.speed, self.is_police)

    def turn(self):
        print(self.name, self.color, 'повернул на право', self.is_police)

    def stop(self):
        print(self.name, self.color, 'остановилась', self.is_police)


car2 = WorkCar('Toyota L200', 'черный', '90', 'is_police')


class PoliceCar:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = True

    def go(self):
        print(self.name, self.color, 'поехала со скоростью', self.speed, self.is_police)

    def turn(self):
        print(self.name, self.color, 'повернул на право', self.is_police)

    def stop(self):
        print(self.name, self.color, 'остановилась', self.is_police)


car3 = PoliceCar('Ford Crown Victoria', 'черно-белый', '200', 'is_police')
car3.stop()

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = False

    def go(self):
        print(self.name, self.color, 'поехала со скоростью', self.speed, self.is_police)

    def turn(self):
        print(self.name, self.color, 'повернул на право', self.is_police)

    def stop(self):
        print(self.name, self.color, 'остановилась', self.is_police)


class TownCar(Car):
    pass


car_ = TownCar('Mersedes E200', 'синий', '120', 'is_police')
car_.stop()


class WorkCar(Car):
    pass


car_1 = WorkCar('Toyota L200', 'черный', '90', 'is_police')

car_1.stop()


class SportCar(Car):
    pass


car_2 = SportCar('Ferrari', 'красный', '250', 'is_police')
car_2.stop()


class PoliceCar(Car):
    pass


car_3 = PoliceCar('Ford Crown Victoria', 'черно-белый', '200', 'is_police')
car_3.stop()

