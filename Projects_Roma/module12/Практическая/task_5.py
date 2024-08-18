print('Задача 5. Текстовый редактор')

# Мы продолжаем разрабатывать новый текстовый редактор,
# и в этот раз нам поручили написать для него код,
# который считает количество любой буквы
# и любой цифры в тексте (а не только буквы Ы как раньше).
#
# Напишите функцию count_letters,
# которая принимает на вход текст и подсчитывает,
# какое в нём количество цифр K и букв N.
#
# Функция должна вывести на экран информацию
# о найденных буквах и цифрах в определенном формате.
#
# Пример:
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищём? л
#
# Количество цифр 0: 2
# Количество букв л: 1


def count_chars(text, digit, letter):
    total_chars_of_letters = 0
    total_number_of_digits = 0
    for _letter in text:
        if _letter == digit:
            total_number_of_digits += 1
        if _letter == letter:
            total_chars_of_letters += 1
    print(f"Количество цифр {digit}: {total_number_of_digits}")
    print(f"Количество букв {letter}: {total_chars_of_letters}")


def program():
    text = input("Напишите текст:\t")
    digit = input("Какую цифру ищем?\t")
    letter = input("Какую букву ищём?\t")
    count_chars(text, digit, letter)


program()
