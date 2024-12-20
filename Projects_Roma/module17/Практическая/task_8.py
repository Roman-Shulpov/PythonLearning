# Задание 8. Шифр Цезаря Что нужно сделать Юлий Цезарь использовал свой способ шифрования текста. Каждая буква
# заменялась на следующую по алфавиту через K позиций по кругу. Если взять русский алфавит и K, равное 3, то в слове,
# которое мы хотим зашифровать, буква А станет буквой Г, Б станет Д и так далее.
#
# Пользователь вводит сообщение и значение сдвига. Напишите программу, которая изменит фразу при помощи шифра Цезаря.
#
# Пример:
#
# Введите сообщение: это питон.
#
# Введите сдвиг: 3
#
# Зашифрованное сообщение: ахс тлхср.


alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у",
            "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]

encrypted_message = ""

message = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

for char in message:
    if char in alphabet:
        index = alphabet.index(char)
        new_index = (index + shift)
        new_serial_number = new_index + 1
        bounded_new_serial_number = new_serial_number % len(alphabet)
        bounded_new_index = bounded_new_serial_number - 1
        encrypted_message += alphabet[bounded_new_index]
    else:
        encrypted_message += char

print(encrypted_message)
print(index)
print(new_index)
