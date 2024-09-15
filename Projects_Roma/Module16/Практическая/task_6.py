# Задание 6. Ролики
# Что нужно сделать
# Частная контора даёт в прокат ролики самых разных размеров. Человек может надеть ролики только своего размера.
# Пользователь вводит два списка размеров: N размеров роликов и K размеров ног людей. Реализуйте код,
# который определяет, какое наибольшее число человек может одновременно взять ролики и пойти кататься.
# Пример:
# Количество роликов: 4
# Размер пары 1: 41
# Размер пары 2: 40
# Размер пары 3: 39
# Размер пары 4: 42
# Количество людей: 3
# Размер ноги человека 1: 42
# Размер ноги человека 2: 41
# Размер ноги человека 3: 42
# Наибольшее количество людей, которые могут взять ролики: 2


foot_sizes = []
roller_sizes = []
number_of_rollers = int(input("Сколько пар роликов будет: "))
rollers_count = 1
for rollers in range(number_of_rollers):
    roller_size = int(input(f"Введите размер {rollers_count} роликов: "))
    rollers_count += 1
    roller_sizes.append(roller_size)
number_of_people = int(input("Сколько человек будет: "))
people_count = 1
for people in range(number_of_people):
    foot_size = int(input(f"Введите размер ноги {people_count} человека: "))
    foot_sizes.append(foot_size)
    people_count += 1

print(f"Размеры роликов: {roller_sizes}")
print(f"Размеры ног людей: {foot_sizes}")
people_skating = 0
if roller_sizes == foot_sizes:
    people_skating += 1

print(f"Наибольшее количество людей, которые могут взять ролики: {people_skating}")

