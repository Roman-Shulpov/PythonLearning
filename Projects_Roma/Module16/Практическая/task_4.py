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
