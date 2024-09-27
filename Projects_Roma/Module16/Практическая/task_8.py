# Задание 8. Симметричная последовательность
# Что нужно сделать
# Последовательность чисел называется симметричной, если она одинаково читается как слева направо, так и
# справа налево. Например, следующие последовательности являются симметричными:
# 1 2 3 4 5 4 3 2 1
# 1 2 1 2 2 1 2 1
# Пользователь вводит последовательность из N чисел. Напишите программу, которая определяет,
# какое минимальное количество и каких чисел нужно добавить в конец этой последовательности, чтобы она стала
# симметричной.
# Пример 1:
# Количество чисел: 5
# Число: 1
# Число: 2
# Число: 1
# Число: 2
# Число: 2
# Последовательность: [1, 2, 1, 2, 2]
# Нужно приписать чисел: 3
# Сами числа: [1, 2, 1]
# Пример 2:
# Количество чисел: 5
# Число: 1
# Число: 2
# Число: 3
# Число: 4
# Число: 5
# Последовательность: [1, 2, 3, 4, 5]
# Нужно приписать чисел: 4
# Сами числа: [4, 3, 2, 1]


def is_palindrome(digit_list):
    half_len = len(digit_list) // 2
    # print(digit_list)
    for i in range(half_len):
        # print(f'Слева: {i + 1}, справа: {len(digit_list) - i}')
        # print(f"Слева: {digit_list[i]} справа {digit_list[len(digit_list) - i - 1]}")
        if digit_list[i] != digit_list[len(digit_list) - i - 1]:
            return False
    return True


digit_list2 = [1, 2, 3, 4, 5, 6]


b = []
while len(digit_list2) > 0:
    print(digit_list2)
    if not is_palindrome(digit_list2):
        b.append(digit_list2.pop(0))
    else:
        break
print(digit_list2)

result_list = b.copy()
result_list.extend(digit_list2)
b.reverse()
result_list.extend(b)
print(result_list)
