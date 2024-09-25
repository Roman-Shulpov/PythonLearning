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

n = int(input("Количество роликов: "))
foot_sizes = []
roller_sizes = []
print("Размер пары роликов:")
for i in range(n):
    foot_sizes.append(int(input(f"Размер пары {i + 1}: ")))
k = int(input("Количество людей: "))
foot_sizes_activity = [False for _ in range(k)]
print("Размер ноги человека:")
for j in range(k):
    roller_sizes.append(int(input(f"Размер ноги человека {j + 1}: ")))
count = 0

for i in range(n):  # цикл перебора всех роликов на складе.
    print(f"---------------------------")
    for j in range(k):
        print(f"i = {i} ({foot_sizes[i]}), j = {j} ({roller_sizes[j]})")

        if foot_sizes[i] == roller_sizes[j] and foot_sizes_activity[i] is False:
            foot_sizes_activity[i] = True
            count += 1
            print("\t\tНашли похожие!")
            print(foot_sizes_activity)
            print(foot_sizes)
print(foot_sizes)
print(roller_sizes)
print(f"{count} человек сможет покататься.")


# зачёт
