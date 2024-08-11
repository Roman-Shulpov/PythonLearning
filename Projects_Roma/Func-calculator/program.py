# еализовать метолды калькулятора
# 1 - сложение двух чисел
# 2 - вычитание двух чисел
# 3 - умножение двух чисел
# 4 - деление числла на число
# 5 - возведение числа в степень
# 6 - вычяисление площади параллелепипеда по 3-м сторонам
#
# обеспечить контроль ввода (функция валидации ввода числа)
#
# программа должа быть зацикленна
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
    if validate_divider(b):
        return a / b


def raise_number_to_power(num, power):
    return num ** power


def calculate_parallelepiped_area(x, y, z):
    result = x * y * z
    print(f'Объём равен - {result}')


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
# ОСНОВНОЙ МЕТОД С ЦИКЛОМ И ВЫХОДОМ (ЗДЕСЬ ИНТЕРФЕЙС ВЫБОРА ДЕЙСТВИЙ С ПОМОЩЬЮ ВВОДА ЧИСЕЛ)
########################################################################################################################


def main():
    while True:
        choice_number = int(input("Выберите действие: 1 - сложить, 2 - вычесть, 3 - умножить, 4 - разделить"
                                  "5 - возвезти в степень, 6 - вычислить площадь параллелепипеда. 0 - выйти."))

        a = 0
        b = 0
        if choice_number in (1, 2, 3, 4):
            while True:
                a_input = input('Введите первое число: ')
                if validate_input_number(a_input):
                    a = int(a_input)
                    break
                else:
                    print("Ошибка ввода! Введите число.")
            while True:
                b_input = input('Введите второе число: ')
                if validate_input_number(b_input):
                    b = int(b_input)
                    break
                else:
                    print("Ошибка ввода! Введите число.")
        # -------------------------------------
        result = None
        if choice_number == 1:
            result = add_numbers(a, b)
            result_output(result)
        elif choice_number == 2:
            result = subtract_numbers(a, b)
            result_output(result)
        elif choice_number == 3:
            result = multiply_numbers(a, b)
            result_output(result)
        elif choice_number == 4:
            result = divide_numbers(a, b)
            result_output(result)
        elif choice_number == 5:
            result = raise_number_to_power(a, b)
            result_output(result)
        elif choice_number == 6:
            while True:
                x_input = input("Введите значение x: ")
                if validate_input_number(x_input):
                    x = int(x_input)
                    break
                else:
                    print("Ошибка ввода! Введите число.")
            while True:
                y_input = input("Введите значение y: ")
                if validate_input_number(y_input):
                    y = int(y_input)
                    break
                else:
                    print("Ошибка ввода! Введите число.")
            while True:
                z_input = input("Введите значение z: ")
                if validate_input_number(z_input):
                    z = int(z_input)
                    break
                else:
                    print("Ошибка ввода! Введите число.")
            calculate_parallelepiped_area(x, y, z)
        # -------------------------------------
        elif choice_number == 0:
            print("Вы вышли из программы!")
            return
        # -------------------------------------
        else:
            print("Такого действия не реализовано!!")


########################################################################################################################
# ЗАПУСК ПРОГРАММЫ
########################################################################################################################


main()
