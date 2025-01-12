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

import os

if os.path.exists('answer.txt'):
    infile = open('answer.txt', 'r')
    content = infile.read()
    infile.close()

    numbers = map(int, content.split())
    total_sum = sum(numbers)

    outfile = open('answer.txt', 'w')
    outfile.write(str(total_sum))
    outfile.close()
else:
    print("Файл numbers.txt не найден.")
