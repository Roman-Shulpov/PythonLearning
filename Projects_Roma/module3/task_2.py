print('Задача 2. Финансовый отчёт')

# Васе пришло очередное задание — автоматизация финансовой отчётности.
# Звучит сложно, а на деле нужно просто написать код, который будет считать нужные для отчёта вычисления автоматически.
# Вычисления, которые нужно реализовать в программе: сумму дохода первых двух кварталов поделить на сумму последних двух кварталов,
# чтобы понять динамику роста или падения дохода.

# Алгоритм действий в программе:
# 1) Запросить у пользователя четыре числа.
# 2) Отдельно сложить два первых и два вторых.
# 3) Разделить первую сумму на вторую.
# 4) Вывести результат на экран.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
d = int(input('Введите четвёртое число: '))

result1 = (a + b)
result2 = (c + d)
print('Результат сложения первого и второго чисел: ', result1)
print('Результат сложения третьего и четвёртого чисел: ', result2)
result3 = 'Результат деления первой полученой суммы и второй: ', result1 / result2
print(result3)
