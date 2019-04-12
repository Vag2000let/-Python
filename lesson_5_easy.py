# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil

# Создает dir_1 - dir_9 циклом
for i in range(1, 10):
    os.mkdir('dir_' + str(i))

# Создает dir_1 - dir_9 в одну строчку
dir_ = [os.mkdir('dir_' + str(i)) for i in range(1, 10)]

print(os.listdir('.'))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

for catalog, dirs, files in os.walk(os.getcwd()):
    print(dirs)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

shutil.copyfile("D:\Lesson_5_easy.py", "D:\copy_Lesson_5_easy.py")