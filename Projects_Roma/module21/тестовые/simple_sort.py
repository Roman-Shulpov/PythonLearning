import random
import time

number_list = [random.randint(0, 1000000) for _ in range(10000)]

print("Исходный список:")
print(number_list)

start_time = time.time()

for _ in range(len(number_list) - 1):
    for index_el in range(len(number_list) - 1):
        if number_list[index_el] > number_list[index_el + 1]:
            number_list[index_el], number_list[index_el + 1] = number_list[index_el + 1], number_list[index_el]

end_time = time.time()
execution_time = end_time - start_time
print(number_list)
print(f"Время выполнения: {execution_time} секунд")
