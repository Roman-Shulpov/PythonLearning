print('Задача 7. Хватит ли зарплаты')

# Вася набрался опыта и решил поискать вакансию с большей зарплатой. Его привлекла вакансия со странной формулой для
# расчёта заработной платы: 200 * hours / 2 ** 3 + hours


# Он хочет понять, сколько часов нужно отработать, чтобы хватило на погашение кредита и еду.

# Напишите программу, которая запрашивает у пользователя три числа: количество отработанных часов, остаток по кредиту и количество денег на еду.

# После этого рассчитывается зарплата по формуле. Если зарплата больше или равна сумме, которая требуется на кредит и еду, то выводится сообщение: «Часов хватает. Можно отдохнуть».
# В противном случае: «Часов не хватает. Придётся работать больше!»

# Пример:
# Введите отработанные часы: 80
# Введите остаток по кредиту: 1000
# Введите траты на еду: 5000
# Часов не хватает. Придётся работать больше!

# hours = int(input('Введите отработанные часы: '))
# credit = int(input('Введите остаток по кредиту: '))
# food = int(input('Введите траты на еду: '))
# salary = hours * 200 / 2 ** 3 + hours
# cost = food + credit
# difference = abs(salary - cost)
#
# if salary < credit + food:
#     print('\nЧасов не хватает. \nПридётся поработать! \n\t(Зарплата = {}, Не хватает = {}, Еда + кредит = {}'
#           .format(salary, difference, cost))
# else:
#     print('\nЧасов хватает. \nМожно отдохнуть \n\t(Зарплата = {}, осталось лишнего = {}, Еда + кредит = {})'
#           .format(salary, difference, cost))


for y in range(-20, 20, 1):
    x = abs(y) ** 2
    print(x, y)
