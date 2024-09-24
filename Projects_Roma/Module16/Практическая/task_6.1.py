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


foot_sizes = [41, 42, 42, 42, 43, 43, 44, 45]
roller_sizes = [41, 42, 41]

fsd = {}
for element in foot_sizes:
    if fsd.get(element) is None:
        fsd.setdefault(element, 1)
    else:
        fsd[element] = fsd[element] + 1
print(fsd)


rsd = {}
for element in roller_sizes:
    if rsd.get(element) is None:
        rsd.setdefault(element, 1)
    else:
        rsd[element] = rsd[element] + 1
print(rsd)


counter = 0
for roller_pair in rsd.items():
    roller_size = roller_pair[0]
    roller_count = roller_pair[1]

    foot_count = fsd.get(roller_size)
    if foot_count is not None:
        if foot_count > roller_count:
            print(f'Размер: {roller_size}. Ботов ({foot_count}) больше, чем роллеров ({roller_count}). '
                  f'Обули {roller_count} роллеров.')
            counter += roller_count
        else:
            print(f'Размер: {roller_size}. Ботов ({foot_count}) меньше, чем роллеров ({roller_count}). '
                  f'Обули {foot_count} роллеров.')
            counter += foot_count
    else:
        print(f'Размер: {roller_size}. Ботов не найдено!')

print(f'Итого обули {counter} роллеров')

# Решение на бустах :D
