# Реализовать метолды калькулятора
# 1 - сложение двух чисел
# 2 - вычитание двух чисел
# 3 - умножение двух чисел
# 4 - деление числа на число
# 5 - возведение числа в степень
# 6 - вычисление площади параллелепипеда по 3-м сторонам
#
# обеспечить контроль ввода (функция валидации ввода числа)
#
# программа должна быть зацикленна
# программа должна иметь консольный интерфейс с выбором действий
# в программе должен быть способ выйти и закончить выполнение программыхх
#
# в программе не должно быть ни одного подчёркивания (ни зелёного, ни красного, ни жёлтого)

########################################################################################################################
# МЕТОДЫ КАЛЬКУЛЯТОРА
########################################################################################################################
########################################################################################################################
# МЕТОДЫ КАЛЬКУЛЯТОРА
########################################################################################################################
def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    return a / b


def raise_number_to_power(num, power):
    return num ** power


def calculate_parallelepiped_area(x, y, z):
    return x * y * z


def result_output(result):
    print(result)


########################################################################################################################
# МЕТОДЫ ВАЛИДАЦИИ
########################################################################################################################

def validate_input_number(input_string):
    try:
        int(input_string)
        return True
    except ValueError:
        return False


def validate_divider(b):
    if b == 0:
        print("Деление на ноль невозможно!")
        return False
    else:
        return True


########################################################################################################################
# ВСПОМОГАТЕЛЬНЫЕ МЕТОДЫ
########################################################################################################################

def input_number(message):
    while True:
        input_num = input(message)
        if validate_input_number(input_num):
            return int(input_num)
        else:
            print("Ошибка ввода! Введите число.")


########################################################################################################################
# ОСНОВНОЙ МЕТОД С ЦИКЛОМ И ВЫХОДОМ (ЗДЕСЬ ИНТЕРФЕЙС ВЫБОРА ДЕЙСТВИЙ С ПОМОЩЬЮ ВВОДА ЧИСЕЛ)
########################################################################################################################

def main():
    while True:
        choice_number = int(input("Выберите действие:\n\t1 - сложить\n\t2 - вычесть\n\t3 - умножить\n\t4 - разделить"
                                  "\n\t5 - возвезти в степень\n\t6 - вычислить площадь "
                                  "параллелепипеда\n--------------------------\n\t0 - выйти."
                                  "\nввод:\t"))

        num1 = 0
        num2 = 0
        if choice_number in (1, 2, 3, 4):
            num1 = input_number("Введите первое число: ")
            num2 = input_number("Введите второе число: ")
        # -------------------------------------
        result = None
        if choice_number == 1:
            result = add_numbers(num1, num2)
        elif choice_number == 2:
            result = subtract_numbers(num1, num2)
        elif choice_number == 3:
            result = multiply_numbers(num1, num2)
        elif choice_number == 4:
            if validate_divider(num2):
                result = divide_numbers(num1, num2)
        elif choice_number == 5:
            result = raise_number_to_power(num1, num2)
        elif choice_number == 6:
            x = input_number("Введите значение x: ")
            y = input_number("Введите значение y: ")
            z = input_number("Введите значение z: ")

            result = calculate_parallelepiped_area(x, y, z)
        # -------------------------------------
        elif choice_number == 0:
            print("Вы вышли из программы!")
            return
        # -------------------------------------
        else:
            print("Такого действия не реализовано!!")

        if result is not None:
            result_output(result)


########################################################################################################################
# ЗАПУСК ПРОГРАММЫ
########################################################################################################################


main()
