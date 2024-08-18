print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример:

# Введите первое число: 102
# Введите второе число: 123


# Первое число наоборот: 201
# Второе число наоборот: 321

# Сумма: 522
# Сумма наоборот: 225

def reverse_float(num):
    parts = str(num).split('.')
    reversed_parts = ''
    for part in parts:
        reversed_part = ''
        for digit in part:
            reversed_part = digit + reversed_part
        reversed_parts += reversed_part
    return float(reversed_parts)


a = reverse_float(input('a: '))
b = reverse_float(input('b: '))
print('перевёрнутое а: ', a)
print('перевёрнутое b: ', b)
print('сумма перевёрнутых чисел: ', a + b)
