print('Задача 6. НОД')

# Напишите функцию, вычисляющую наибольший общий делитель двух чисел


def program():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    if a != 0 and b != 0:
        if a > b:
            a = a % b
        elif a < b:
            b = b % a
    print(a + b)


program()
