print('Задача 2. Посчитай чужую зарплату...')

# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании
# и, чтобы облегчить себе жизнь, обратилась к программисту.

# Напишите программу,
# которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев
# и выводит на экран среднюю зарплату за год.

year_salary = 0
month = 1
for i in range(0, 12):
    monthly_salary = int(input(f"Введите вашу зарплату за {month} месяц: "))
    month += 1
    year_salary += monthly_salary
print(f'Ваша средняя зарплата за год: {year_salary} руб.')
