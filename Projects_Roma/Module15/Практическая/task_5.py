n = int(input('Сколько всего контейнеров: '))
containers = []
for i in range(n):
    while True:
        print('Введите вес', i + 1, 'контейнера: ', end=' ')
        weight = int(input())
        if 0 < weight < 200:
            containers.append(weight)
            break
        else:
            print('Вес контейнера должен быть больше 0 и меньше 200')
new = int(input('Введите вес нового контейнера: '))
while new < 1 or new > 200:
    print('Неверный вес, попробуйте ещё раз')
    new = int(input('Введите вес нового контейнера: '))

index = 0
for i in containers:
    if i < new:
        break
    index += 1
print('Номер, который получит новый контейнер:', index + 1)
