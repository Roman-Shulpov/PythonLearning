number_list = []
number = int(input('Введите число: '))

for i in range(1, number + 1):
    if i % 2 != 0:
        number_list.append(i)

print(f'\nСписок из нечётных чисел от одного до {number}:', number_list)
