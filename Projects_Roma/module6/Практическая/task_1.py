print('Задача 1. Кубы чисел')

# В один из вечеров к Васе домой пришёл племянник и пожаловался на сложности с уроками математики:
# у него никак не получалось разобраться со степенями чисел.
# Вася решил помочь племяннику и написать программу,
# которая позволит наглядно увидеть возведение чисел в третью степень.

# Напишите программу, которая возводит в третью степень каждое число от 1 до N и выводит результат на экран.

# Пример
# Введите число: 3
# 1 ** 3 = 1
# 2 ** 3 = 8
# 3 ** 3 = 27

count = 1
n = int(input('Введите число: '))
while count <= n:
    print(count ** n)
    count += 1
