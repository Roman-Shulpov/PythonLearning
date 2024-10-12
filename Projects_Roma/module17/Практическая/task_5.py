# Задание 5. Разворот
# Что нужно сделать
# На вход в программу подаётся строка, в которой буква h встречается как минимум два раза. Реализуйте код,
# который разворачивает последовательность символов, заключённую между первым и последним появлением буквы h, в
# противоположном порядке.
#
# Пример 1:
#
# Введите строку: hqwehrty
#
# Развёрнутая последовательность между первым и последним h: ewq.
#
# Пример 2:
#
# Введите строку: hh
#
# Развёрнутая последовательность между первым и последним h:
#
# Пример 3:
#
# Введите строку: hhqwerh
#
# Развёрнутая последовательность между первым и последним h: rewqh.


def get_reversed_boundary_substring(source_string, boundary_symbol):
    first_index = None
    last_index = None
    for i in range(len(source_string)):
        if source_string[i] == boundary_symbol:
            if first_index is None:
                first_index = i
            last_index = i
    if first_index is not None and last_index is not None and first_index != last_index:
        substring = source_string[first_index + 1:last_index]
        reversed_substring = substring[::-1]
        return reversed_substring


our_string = input("Введите строку:\t")
our_boundary_symbol = "k"
our_reversed_substring = get_reversed_boundary_substring(our_string, our_boundary_symbol)
print(f"Развёрнутая последовательность между первым и последним {our_boundary_symbol}:", our_reversed_substring)

