# Задача 6. «Война и мир» Что нужно сделать Мало кто не знает знаменитый роман Л. Н. Толстого «Война и мир». Это
# довольно объёмное произведение лежит в архиве voina-i-mir.zip. Напишите программу, которая подсчитывает статистику
# по буквам (не только русского алфавита) в этом романе и выводит результат на экран (или в файл). Результат должен
# быть отсортирован по частоте встречаемости букв (по возрастанию или убыванию). Регистр символов имеет значение.
#
# Архив можно распаковать вручную, но, если хотите, можете изучить документацию по модулю zipfile (можно использовать
# и другой модуль) и попробовать написать код, который будет распаковывать архив за вас.
#
# Что оценивается
# Результат вычислений корректен.
# Основной функционал описан в отдельных функциях.
# Переменные и функции имеют значащие имена, а не только a, b, c, d (подробнее об этом в видео 2.3).
# Входной файл назван так, как указано в задании, выходной файл имеет значащее имя.

import zipfile
from collections import Counter


def extract_text_from_zip(zip_filename, text_filename):
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extract(text_filename)


def read_text_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def analyze_letter_frequency(text):
    letter_count = Counter(text)
    total_letters = sum(letter_count.values())
    frequency = {char: count / total_letters for char, count in letter_count.items() if char.isalpha()}
    return frequency


def write_frequency_to_file(filename, frequency):
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1])
    with open(filename, 'w', encoding='utf-8') as file:
        for letter, freq in sorted_frequency:
            file.write(f"{letter} {freq:.3f}\n")


def main():
    zip_filename = 'voina-i-mir.zip'
    text_filename = 'voina-i-mir.txt'
    extract_text_from_zip(zip_filename, text_filename)
    text = read_text_file(text_filename)
    frequency = analyze_letter_frequency(text)
    write_frequency_to_file('letter_frequency_analysis.txt', frequency)


if __name__ == "__main__":
    main()
