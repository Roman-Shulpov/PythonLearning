# Задание 1. Песни — 2
# Что нужно сделать
# Продолжим писать приложение для удобного прослушивания музыки, но теперь песни хранятся в виде словаря, а
# не в виде вложенных списков. Каждая песня состоит из названия и продолжительности с точностью до долей минут.
#
# violator_songs = {
# 'World in My Eyes': 4.86,
# 'Sweetest Perfection': 4.43,
# 'Personal Jesus': 4.56,
# 'Halo': 4.9,
# 'Waiting for the Night': 6.07,
# 'Enjoy the Silence': 4.20,
# 'Policy of Truth': 4.76,
# 'Blue Dress': 4.29,
# 'Clean': 5.83
# }
# Напишите программу, которая запрашивает у пользователя количество песен из списка и их названия, а на экран
# выводит общее время их звучания.

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

time = 0

number_of_songs = int(input("Введите количество песен: "))
for song in range(number_of_songs):
    song_name = input("Введите название песни: ")
    song_value = violator_songs.get(song_name)
    if song_value is not None:
        time += song_value

print(round(time), 2)
