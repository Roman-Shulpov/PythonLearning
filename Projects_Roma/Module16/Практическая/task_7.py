# Задание 7. Считалка
# Что нужно сделать
# N человек, пронумерованных числами от 1 до N, стоят в кругу. Они начинают играть в считалку на выбывание.
# Каждый K-й по счёту человек выходит из круга, после чего счёт продолжается со следующего за ним человека.
# На вход подаётся количество человек N и номер K. Напишите программу, которая выводит число от 1 до N — это
# номер человека, который останется в кругу последним.
# Пример:
# Количество человек: 5
# Какое число в считалке? 7
# Значит, выбывает каждый 7-й человек
# Текущий круг людей: [1, 2, 3, 4, 5]
# Начало счёта с номера 1
# Выбывает человек под номером 2
# Текущий круг людей: [1, 3, 4, 5]
# Начало счёта с номера 3
# Выбывает человек под номером 5
# Текущий круг людей: [1, 3, 4]
# Начало счёта с номера 1
# Выбывает человек под номером 1
# Текущий круг людей: [3, 4]
# Начало счёта с номера 3
# Выбывает человек под номером 3
# Остался человек под номером 4

people = int(input('Кол-во человек: '))
number = int(input('Какое число в считалке? '))
print(f'Значит выбывает каждый {number}-й человек')
list_people = list(range(1, people + 1))
start = 0
while len(list_people) > 0:
    print('Текущий круг людей: ', list_people)

print('Остался человек под номером', list_people)

# TODO не работает, нужно тестировать свой код
#
# ТЕСТ 1
#
# Количество человек: 5
# Какое число в считалке? 7