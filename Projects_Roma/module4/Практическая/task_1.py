print('Задача 1. Датчик погоды')

# В за окном квартиры стоит датчик погоды, который определяет, идёт ли дождь. Если идёт, датчик оповещает сообщением: «Пошёл дождь. Возьмите зонтик!»

# Напишите программу, которая получает на вход число 0 или 1. Единица означает, что дождь идёт. В таком случае выводите на экран сообщение: «Пошёл дождь.

# Возьмите зонтик!». Ноль означает, что дождя нет, в этом случае надо вывести сообщение «Дождя нет!»

# Пример 1:
weather = int(input('На улице идёт дождь? Введите - "0", если не идёт, а если идёт, введите число - "1": '))
if weather == 0:
    print('На улице дождя нет.')
if weather == 1:
    print('На улице идёт дождь, возьмите зонтик!')
