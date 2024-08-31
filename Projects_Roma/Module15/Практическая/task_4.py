n = int(input('Сколько фильмов хотите добавить? '))
films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон',
         'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
favorite_films_list = []
for _ in range(n):
    film_name = input('Введите название фильма: ')
    if film_name in films:
        favorite_films_list.append(film_name)
    else:
        print('Ошибка: фильма', film_name, 'у нас нет :(')
print('Ваш список любимых фильмов: ', end='')
print(*favorite_films_list, sep=', ')
