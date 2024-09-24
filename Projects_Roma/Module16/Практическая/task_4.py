# Задание 4. Вечеринка
# Что нужно сделать
# В честь своего дня рождения Артём решил закатить вечеринку у себя на даче. Он не стал рассылать приглашения, а просто
# сообщил всем: «Если хотите — приходите и своих друзей тоже зовите». Во время вечеринки люди приходили и уходили,
# ночевать остались не все. К тому же на даче помещается всего шесть человек.
# Дан изначальный список гостей — имена тех, кто пришёл к началу:
#
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
# Напишите программу, которая спрашивает у пользователя, ушёл ли человек и пришёл ли новый гость, и, исходя из ответа,
# добавляет в список или удаляет из него нужное имя. При этом гостей может быть не больше шести. Имена запрашиваются до
# тех пор, пока пользователь не введёт сообщение «Пора спать».
# Пример:
# Сейчас на вечеринке 5 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’]
# Гость пришёл или ушёл? Пришёл
# Имя гостя: Алекс
# Привет, Алекс!
# Сейчас на вечеринке 6 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’, ‘Алекс’]
# Гость пришёл или ушёл? пришёл
# Имя гостя: Гоша
# Прости, Гоша, но мест нет.
# Сейчас на вечеринке 6 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’, ‘Алекс’]
# Гость пришёл или ушёл? ушёл
# Имя гостя: Ваня
# Пока, Ваня!
# Сейчас на вечеринке 5 человек: [‘Петя’, ‘Саша’, ‘Лиза’, ‘Катя’, ‘Алекс’]
# Гость пришёл или ушёл? Пора спать
# Вечеринка закончилась, все легли спать.

SEATS_COUNT = 6
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
while True:
    print(f'\n\nСейчас на вечеринке {len(guests)} человек: {guests}')
    answer = input('\nГость пришёл или ушёл? ').lower()
    if answer == 'пора спать':
        print('\nВечеринка закончилась, все легли спать.')
        break
    name = input('\nИмя гостя: ')
    if answer in ['пришёл', 'пришел']:
        if len(guests) == SEATS_COUNT:
            print(f'\nПрости, {name}, но мест нет.')
        else:
            print(f'\nПривет, {name}!')
            guests.append(name)
    else:
        print(f'\nПока, {name}!')
        guests.remove(name)
# Зачтено!