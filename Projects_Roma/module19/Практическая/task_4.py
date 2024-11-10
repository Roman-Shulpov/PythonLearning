# Задание 4. Гистограмма частоты — 2
# Что нужно сделать
# Вы уже писали программу для лингвистов, которая получала на вход текст и считала, сколько раз каждый символ встречается
# в строке. Теперь задание изменилось: максимальную частоту выводить не нужно, но необходимо написать функцию, которая
# будет инвертировать полученный словарь. То есть в качестве ключа будет частота, а в качестве значения — список символов
# с этой частотой.
#
# По итогу нужно реализовать следующие подзадачи:
#
# получить текст и создать из него оригинальный словарь частот;
# создать новый словарь и заполнить его данными из оригинального словаря частот, используя количество повторов в качестве
# ключей, а буквы — в качестве значений, добавляя их в список для хранения.
# Пример
#
# Введите текст: здесь что-то написано
#
# Оригинальный словарь частот:
#
# : 2
#
# - : 1
#
# З : 1
#
# а : 2
#
# д : 1
#
# е : 1
#
# и : 1
#
# н : 2
#
# о : 3
#
# п : 1
#
# с : 2
#
# т : 2
#
# ч : 1
#
# ь : 1
#
# Инвертированный словарь частот:
#
# 1 : ['З', 'д', 'е', 'ь', 'ч', '-', 'п', 'и']
#
# 2 : ['с', ' ', 'т', 'н', 'а']
#
# 3 : ['о']

def calculate_frequency(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency



def invert_frequency(frequency):
    inverted_frequency = {}
    for char, freq in frequency.items():
        if freq in inverted_frequency:
            inverted_frequency[freq].append(char)
        else:
            inverted_frequency[freq] = [char]
    return inverted_frequency


text = input("Введите текст: ")
original_frequency = calculate_frequency(text)

print("\nОригинальный словарь частот:")
for char, freq in original_frequency.items():
    print(f"{char}: {freq}")

inverted_frequency = invert_frequency(original_frequency)

print("\nИнвертированный словарь частот:")
for freq, chars in sorted(inverted_frequency.items()):
    print(f"{freq}: {chars}")
