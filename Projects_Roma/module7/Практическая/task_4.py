print('Задача 4. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было.
#
# Напишите программу,
# которая получает список оценок - N чисел - и выводит на экран сообщение о том,
# кого сегодня больше: отличников, хорошистов или троечников.

# Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.

threes = 0
fours = 0
fives = 0
students_number = 1
students = 11

for i in range(students):
    assessment = int(input(f'Какую оценку получил {students_number} ученик? : '))
    students_number += 1

    if assessment == 3:
        threes += 1
    elif assessment == 4:
        fours += 1
    elif assessment == 5:
        fives += 1

if (fives > fours) and (fives > threes):
    print(f'Сегодня больше всего отличников! Их количество: {fives}')
elif (fours > fives) and (fours > threes):
    print(f'Сегодня больше всего хорошистов! Их количество: {fours}')
elif (threes > fives) and (threes > fours):
    print(f'Сегодня больше всего троечников! Их количество: {threes}')

elif (threes == fours) and (threes == fives) and (fours == fives):
    print('Сегодня всё поровну.')
