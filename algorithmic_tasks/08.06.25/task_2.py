import my_utils
import random


def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == target:
            return mid  # Возвращаем индекс найденного элемента
        elif lst[mid] > target:
            right = mid - 1  # Продолжаем поиск слева
        else:
            left = mid + 1  # Продолжаем поиск справа

    return None  # Если элемент не найден


# Тестируем функцию

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
# lst = my_utils.generate_list(21, 0, 100)
lst.sort()
print(lst)
target =
result = binary_search(lst, target)
if result is not None:
    print(f'Элемент {target} найден на позиции {result + 1}')
else:
    print('Элемент не найден')
