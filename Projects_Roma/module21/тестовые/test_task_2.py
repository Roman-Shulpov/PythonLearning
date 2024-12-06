def partition(lst):
    if not lst:
        return [], [], []

    pivot = lst[-1]
    less_than = []
    equal_to = []
    greater_than = []

    for item in lst:
        if item < pivot:
            less_than.append(item)
        elif item == pivot:
            equal_to.append(item)
        else:
            greater_than.append(item)

    return less_than, equal_to, greater_than


def quicksort(lst):
    if len(lst) <= 1:
        return lst

    less_than, equal_to, greater_than = partition(lst)

    sorted_less = quicksort(less_than)
    sorted_greater = quicksort(greater_than)

    return sorted_less + equal_to + sorted_greater


# Пример использования
numbers = [4, 9, 2, 7, 5]
sorted_numbers = quicksort(numbers)
print(sorted_numbers)
