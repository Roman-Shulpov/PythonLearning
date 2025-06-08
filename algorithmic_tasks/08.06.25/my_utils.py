import time
import random


def time_of_function(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter_ns()
        res = func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        elapsed_time = end_time - start_time
        minutes = elapsed_time // (60 * 10**9)
        seconds = (elapsed_time % (60 * 10**9)) // 10**9
        milliseconds = (elapsed_time % 10**9) // 10**6
        print(f"Функция {func.__name__} выполнилась за {minutes} м. {seconds} с. {milliseconds} мс.")
        return res
    return wrapper


def generate_list(n, min_rand_num, max_rand_num):
    array = []
    for _ in range(n):
        num = random.randint(min_rand_num, max_rand_num + 1)
        array.append(num)
    return array
