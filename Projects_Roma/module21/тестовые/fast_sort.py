# сделать быструю сортировку.
import random
import time  # Импортируем модуль time

def quick_sort(arr):
    size = len(arr)
    if size <= 1:
        return arr
    pivot = arr[size // 2]  # Выбор опорного элемента
    left = [x for x in arr if x < pivot]  # Элементы меньше опорного
    middle = [x for x in arr if x == pivot]  # Элементы равные опорному
    right = [x for x in arr if x > pivot]  # Элементы больше опорного
    return quick_sort(left) + middle + quick_sort(right)


# Пример использования
array = [random.randint(0, 1000000) for _ in range(1000000)]

# Измеряем время выполнения сортировки
start_time = time.time()  # Запоминаем начальное время

start_size = len(array)

sorted_array = quick_sort(array)
end_time = time.time()  # Запоминаем конечное время

# Выводим отсортированный массив и время выполнения
print("Отсортированный массив:", sorted_array)
print("Время выполнения сортировки: {:.6f} секунд".format(end_time - start_time))
