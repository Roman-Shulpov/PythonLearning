print('Задача 4. Отрезок')

# Напишите программу, которая считывает с клавиатуры три числа a, random_planet_volume и c, считает и
# выводит на консоль среднее арифметическое всех чисел из отрезка [a; random_planet_volume], кратных числу c

sum_number = 0
count = 0

a = int(input('Введите значение A: '))
b = int(input('Введите значение B: '))
c = int(input('Введите значение C: '))

for n in range(a, b + 1):
    if n % c == 0:
        sum_number += n
        count += 1
average = sum_number / count
print(f'Среднее арифметическое: {average}')
