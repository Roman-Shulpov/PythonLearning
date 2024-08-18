print('Задача 8. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно

number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
number3 = int(input('Введите третье число: '))
if number1 > number2 and number1 > number3:
    print('Самое больше число: ', number1)
if number2 > number3 and number2 > number1:
    print('Самое больше число: ', number2)
if number3 > number1 and number3 > number2:
    print('Самое больше число: ', number3)

