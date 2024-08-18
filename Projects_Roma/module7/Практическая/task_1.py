print('Задача 1. Должники')

# В базе банка хранятся данные и должников, и законопослушных граждан. Каждому человеку система присваивает свой номер.
# У нас есть случайная выборка из десяти номеров. Правда, иногда база глючит и выдаёт номер с отрицательным значением.
# А ещё по статистике, которую собрал наш «МирПрогБанк», каждый второй пользователь брал кредит и не выплатил его вовремя,
# то есть является должником.

# Напишите программу, которая при вводе десяти чисел определяет, сколько из них являются одновременно чётными и положительными.

resultat = 0
for i in range(0, 10):
    numbers = int(input('Введите 10 чисел: '))
    if numbers % 2 == 0 and numbers > 0:
        resultat += 1
print('Всего чётных и в то же время положительных чисел: ', resultat)
