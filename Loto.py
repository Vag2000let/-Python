import random

"""
== Лото ==
Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90

 2    27    75 78    82

   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)

------ Ваша карточка -----

 6  7          49    57 58

   14 26     -    78    85

23 33    38    48    71
--------------------------

-- Карточка компьютера ---

 7 11     - 14    87

      16 49    55 77    88

   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""


class Game:
    def __init__(self, barrel, count_barrel, useranswer):
        self.barrel = barrel
        self.count_barrel = count_barrel
        self.useranswer = useranswer
        self.line1 = [random.randrange(1, 90) for _ in range(5)]
        self.line2 = [random.randrange(1, 90) for _ in range(5)]
        self.line3 = [random.randrange(1, 90) for _ in range(5)]
        self.line4 = [random.randrange(1, 90) for _ in range(5)]
        self.line5 = [random.randrange(1, 90) for _ in range(5)]
        self.line6 = [random.randrange(1, 90) for _ in range(5)]

    def count_bar(self):
        while True:
            self.count_barrel = 90
            self.barrel = random.randrange(1, 90)
            self.count_barrel -= 1
            print('Новый бочонок :', self.barrel, 'осталось:', self.count_barrel)
            print('--- Ваша карточка ---\n', self.line1, '\n', self.line2, '\n', self.line3, '\n', '-' * 25)
            print('--- Карточка компьютера ---\n', self.line4, '\n', self.line5, '\n', self.line6, '\n', '-' * 25)
            for i in self.line4 and self.line5 and self.line6:
                if i == self.barrel:
                    self.line4[i] = '-'
                    print(self.line4)
                    self.line5[i] = '-'
                    print(self.line5)
                    self.line6[i] = '-'
                    print(self.line6)
            self.useranswer = input('Зачеркнуть цифру? (y/n): ')
            if self.useranswer == 'y':
                for i in self.line1 and self.line2 and self.line3:
                    if i == self.barrel:
                        self.line1[i] = '-'
                        print(self.line1)
                        self.line2[i] = '-'
                        print(self.line2)
                        self.line3[i] = '-'
                        print(self.line3)
            elif self.useranswer == 'n':
                continue


my_game = Game('barrel', 'count_barrel', 'useranswer')
my_game.count_bar()