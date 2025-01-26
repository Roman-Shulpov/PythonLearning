# Задача 3. Файлы и папки Что нужно сделать Напишите программу, которая получает на вход путь до каталога (в том
# числе это может быть просто корень диска) и выводит общее количество файлов и подкаталогов в нём. Также выведите на
# экран размер каталога в килобайтах (1 килобайт = 1024 байт).
#
# Важный момент: чтобы посчитать, сколько весит каталог, нужно найти сумму размеров всех вложенных в него файлов.
#
# Результат работы программы на примере python_basic\Module14:
#
# E:\PycharmProjects\python_basic\Module14
#
# Размер каталога (в Кбайтах): 8.373046875
#
# Количество подкаталогов: 7
#
# Количество файлов: 15
#
# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Input содержит корректные приглашения для ввода.
# Основной функционал описан в отдельных функциях.
# Переменные и функции имеют значащие имена, а не только a, b, c, d (подробнее об этом в видео 2.3).
#


import os


def get_directory_info(path):
    total_size = 0
    file_count = 0
    dir_count = 0

    for root, dirs, files in os.walk(path):
        dir_count += len(dirs)
        file_count += len(files)
        for file in files:
            total_size += os.path.getsize(os.path.join(root, file))

    return total_size, file_count, dir_count


def main():
    path = input("Введите путь до каталога: ")
    total_size, file_count, dir_count = get_directory_info(path)
    size_in_kb = total_size / 1024
    print(f"Размер каталога (в Кбайтах): {size_in_kb:.9f}")
    print(f"Количество подкаталогов: {dir_count}")
    print(f"Количество файлов: {file_count}")


if __name__ == "__main__":
    main()

