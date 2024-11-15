# Задача 4. По парам Что нужно сделать Напишите программу, которая инициализирует список из 10 случайных целых чисел,
# а затем делит эти числа на пары кортежей внутри списка. Выведите результат на экран.
#
# Дополнительно: решите задачу несколькими способами.
#
# Пример:
#
# Оригинальный список: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Новый список: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
#
# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значимые имена, не только a, b, c, d.
# Для решения используются list comprehensions.

original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = [(original_list[i], original_list[i + 1]) for i in range(0, len(original_list), 2)]

print(new_list)
