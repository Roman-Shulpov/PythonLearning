print('Задача 2. Лестница')

# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

number_of_steps = int(input('Введите количество ступеней: '))
for row in range(number_of_steps + 1):
    for col in range(row):
        print(row, end=' ')
    print(' ')
