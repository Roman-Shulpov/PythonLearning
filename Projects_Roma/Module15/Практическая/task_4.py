n = int(input('Сколько фильмов хотите добавить? '))
films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон',
         'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
favorite = []
for _ in range(n):
    name_film = input('Введите название фильма: ')
    if name_film in films:
        favorite.append(name_film)
    else:
        print('Ошибка: фильма', name_film, 'у нас нет :(')
print('Ваш список любимых фильмов: ', end='')
print(*favorite, sep=', ')

