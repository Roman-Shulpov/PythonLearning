# Задача 1. Сумма чисел 2 Что нужно сделать Во входном файле numbers.txt записано N целых чисел, которые могут быть
# разделены пробелами и концами строк. Напишите программу, которая выводит сумму чисел во выходной файл answer.txt.
#
# Пример:
#
# Содержимое файла numbers.txt
#      2
# 2
#   2
#         2
#
# Содержимое файла answer.txt
#
# 8
#
# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Основной функционал описан в отдельных функциях.
# Переменные и функции имеют значащие имена, а не только a, b, c, d (подробнее об этом в видео 2.3).
# Входные и выходные файлы названы так, как указано в задании.

def read_numbers_from_file(filename):
    with open('numbers.txt', 'r') as file:
        content = file.read()
        print()
    numbers = content.split()
    return numbers


def write_sum_to_file(filename, total):
    with open(filename, 'w') as file:
        file.write(str(total))


def main():
    numbers = read_numbers_from_file('numbers.txt')
    total = sum(numbers)
    write_sum_to_file('answer.txt', total)


if __name__ == "__main__":
    main()

