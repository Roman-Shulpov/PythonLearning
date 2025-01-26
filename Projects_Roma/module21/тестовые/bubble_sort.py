# сделать пузырьковую сортировку.
import random
import os
import time  # Импортируем модуль time


# Сделать пузырьковую сортировку.
def bubble_sort(arr):
    n = len(arr)
    # Проходим по всем элементам массива
    for i in range(n):
        # Флаг для отслеживания необходимости дальнейшей сортировки
        swapped = False
        # Последние i элементов уже отсортированы
        for j in range(0, n - i - 1):
            # Сравниваем соседние элементы
            if arr[j] > arr[j + 1]:
                # Меняем местами, если элементы в неправильном порядке
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Если за проход не было обменов, массив уже отсортирован
        if not swapped:
            break
    return arr


# Пример использования
array = [random.randint(0, 1000000) for _ in range(25000)]

# Измеряем время выполнения сортировки
start_time = time.time()  # Запоминаем начальное время
sorted_array = bubble_sort(array)
end_time = time.time()  # Запоминаем конечное время

# Выводим отсортированный массив и время выполнения
print("Отсортированный массив:", sorted_array)
print("Время выполнения сортировки: {:.6f} секунд".format(end_time - start_time))
