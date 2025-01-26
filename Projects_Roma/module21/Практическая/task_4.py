# Задача 4. Продвинутая функция sum Что нужно сделать Как вы знаете, в Python есть полезная функция sum,
# которая умеет находить сумму элементов списков. Иногда базовых возможностей функций не хватает для работы и
# приходится их усовершенствовать.
#
# Напишите свою функцию sum, которая должна быть более гибкой, чем стандартная. Она должна уметь складывать числа:
#
# из списка списков,
# набора параметров.
# Основной код оставьте пустым или закомментированным (используйте его только для тестирования).
#
# Примеры вызовов функции
#
# sum([[1, 2, [3]], [1], 3])
#
# Ответ в консоли: 10
#
# sum(1, 2, 3, 4, 5)
#
# Ответ в консоли: 15


def simple_sum(*args):
    total = 0

    for arg in args:
        if isinstance(arg, list):
            total += simple_sum(*arg)
        else:
            total += arg

    return total


print("Ответ в консоли: ", simple_sum(1, 2, 3, 4, 5))
print("Ответ в консоли: ", simple_sum([1, [2, [3]], 4]))
