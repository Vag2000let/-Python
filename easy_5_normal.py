import os

# Создание новой папки
def create_dir():
    d = input('Введите название папки: ')
    try:
        os.mkdir(d)
        print('Успешно создано!')
    except FileExistsError:
        print('Папка уже существует!')

# Выбор папки
def change_dir():
    a = input('Введите название папки: ')
    try:
        os.chdir(a)
        print('Успешно перешел!')
    except FileExistsError:
        print('Не возможно перейти!')

# Папки текущей директории.
def now():
    print(os.listdir('.'))

# Удаление папки
def del_dir():
    d = input('Введите название папки: ')
    try:
        os.mkdir(d)
        print('Успешно удалена!')
    except FileExistsError:
        print('Невозможно удалить!')