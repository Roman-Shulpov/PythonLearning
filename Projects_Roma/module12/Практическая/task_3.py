print('Задача 3. Апгрейд калькулятора')


# Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются не только обычные
# арифметические действия.
# Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.

# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом: вывести сумму
# его цифр, максимальную или минимальную цифру.

# Каждое действие оформите в виде отдельной функции, а основную программу зациклите.

# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.


def calculator():
    global resultat
    n = int(input("Введите первое число: "))
    n_1 = n // 10
    n_2 = n % 10
    question = input("Что будем делать с первой и последней цифрой? \n '-' вычитать, '+' - складывать\n '/' "
                     "- делить, '*' - умножать.\n: ")
    if question == "-":
        resultat = n_1 - n_2
    elif question == "+":
        resultat = n_1 + n_2
    elif question == "/":
        resultat = n_1 / n_2
    elif question == "*":
        resultat = n_1 * n_2
    else:
        print("ошибка")
    print("Получается: ", resultat)


while True:
    calculator()
