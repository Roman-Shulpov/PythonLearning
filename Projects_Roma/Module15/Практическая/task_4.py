n = int(input('Сколько фильмов хотите добавить? '))
films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон',
         'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
favorite = []  # TODO изменить нейминг
for _ in range(n):
    film_name = input('Введите название фильма: ')
    if film_name in films:
        favorite.append(film_name)
    else:
        print('Ошибка: фильма', film_name, 'у нас нет :(')
print('Ваш список любимых фильмов: ', end='')  # TODO Зачем end?
print(*favorite, sep=', ')  # TODO рассказать как работает, + sep это?

# TODO добавить слова в словарь, чтобы пропали подчеркивания