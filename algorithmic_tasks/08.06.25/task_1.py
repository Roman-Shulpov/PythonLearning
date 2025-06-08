import my_utils


@my_utils.time_of_function
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


array = my_utils.generate_list(10000, 0, 1000000)
print(array)
array_sort = bubble_sort(array)
print(array_sort)
