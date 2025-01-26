# Задача 5. Частотный анализ Что нужно сделать Есть файл text.txt, который содержит текст. Напишите программу,
# которая выполняет частотный анализ, определяя долю каждой буквы английского алфавита в общем количестве английских
# букв в тексте, и выводит результат в файл analysis.txt. Символы, не являющиеся буквами английского алфавита,
# учитывать не нужно.
#
# В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте, с тремя знаками в дробной части. Буквы
# должны быть отсортированы по убыванию их доли. Буквы с равной долей должны следовать в алфавитном порядке.
#
# Пример:
#
# Содержимое файла text.txt:
#
# Mama myla ramu.
#
# Содержимое файла analysis.txt:
#
# a 0.333
#
# m 0.333
#
# l 0.083
#
# r 0.083
#
# u 0.083
#
# y 0.083
#
# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Основной функционал описан в отдельных функциях.
# Переменные и функции имеют значащие имена, а не только a, b, c, d (подробнее об этом в видео 2.3).
# Входные и выходные файлы названы так, как указано в задании.

def read_text_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def analyze_frequency(text):
    text = text.lower()
    letter_count = {}
    total_letters = 0

    for char in text:
        if char.isalpha():
            total_letters += 1
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    frequency = {letter: count / total_letters for letter, count in letter_count.items()}
    return frequency

def write_analysis_to_file(filename, frequency):
    sorted_frequency = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
    with open(filename, 'w') as file:
        for letter, freq in sorted_frequency:
            file.write(f"{letter} {freq:.3f}\n")

def main():
    text = read_text_file('text.txt')
    frequency = analyze_frequency(text)
    write_analysis_to_file('analysis.txt', frequency)

if __name__ == "__main__":
    main()
