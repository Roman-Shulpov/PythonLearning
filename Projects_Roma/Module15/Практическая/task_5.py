n = int(input('Сколько всего контейнеров: '))
containers = []
for container in range(n):
    while True:
        weight = int(input(f'Введите вес {container + 1} контейнера:'))
        if 0 < weight < 200:
            containers.append(weight)
            break
        else:
            print('Вес контейнера должен быть больше 0 и меньше 200')
new_container_weight = int(input('Введите вес нового контейнера: '))
while new_container_weight < 1 or new_container_weight > 200:
    print('Неверный вес, попробуйте ещё раз')
    new_container_weight = int(input('Введите вес нового контейнера: '))

index = 0
for container in containers:
    if container < new_container_weight:
        break
    index += 1
print('Номер, который получит новый контейнер:', index + 1)