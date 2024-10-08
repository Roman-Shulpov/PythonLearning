print('Задача 1. Космическая еда')

# Ваш космический корабль потерпел крушение на пустынной планете. Еда здесь не растёт,
# но вы спасли из обломков 100-килограммовый мешок гречки. Из прошлого опыта вы знаете,
# что если будете экономно питаться, то у вас будет уходить по четыре килограмма гречки в месяц.

# Чтобы прикинуть гречневый бюджет, вы решили написать программу, которая выведет информацию о том,
# сколько килограммов гречки у вас должно быть в запасе через месяц, два и так далее, пока она не закончится.
# Используйте цикл for.

buckwheat = 100
month_eating_buckwheat = 4
month = 1

for _ in range(buckwheat // 4):
    print(f'Месяц {month}, на следущий месяц осталось {buckwheat - month_eating_buckwheat} кг гречки.')
    buckwheat -= month_eating_buckwheat
    month += 1
