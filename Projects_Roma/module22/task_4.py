# Задача 4. Турнир Что нужно сделать В файле first_tour.txt записано число K и данные об участниках турнира по
# настольной игре «Орлеан»: фамилии, имена и количество баллов, набранных в первом туре. Во второй тур проходят
# участники, которые набрали более K баллов в первом туре.
#
# Напишите программу, которая выводит в файл second_tour.txt данные всех участников, прошедших во второй тур,
# с нумерацией.
#
# В первой строке нужно вывести в файл second_tour.txt количество участников второго тура. Затем программа должна
# вывести фамилии, инициалы и количество баллов всех участников, прошедших во второй тур, с нумерацией. Имя нужно
# сократить до одной буквы. Список должен быть отсортирован по убыванию набранных баллов.
#
# Пример:
#
# Содержимое файла first_tour.txt:
#
# 80
#
# Ivanov Serg 80
#
# Sergeev Petr 92
#
# Petrov Vasiliy 98
#
# Vasiliev Maxim 78
#
# Содержимое файла second_tour.txt:
#
# 2
#
# 1) V. Petrov 98
#
# 2) P. Sergeev 92
#
# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Основной функционал описан в отдельных функциях.
# Переменные и функции имеют значащие имена, а не только a, b, c, d (подробнее об этом в видео 2.3).
# Входные и выходные файлы названы так, как указано в задании.

def read_tournament_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    k = int(lines[0].strip())
    participants = []
    for line in lines[1:]:
        name, surname, score = line.strip().split()
        participants.append((surname, name, int(score)))
    return k, participants

def filter_and_sort_participants(k, participants):
    qualified = [p for p in participants if p[2] > k]
    return sorted(qualified, key=lambda x: x[2], reverse=True)

def write_second_tour_data(filename, qualified):
    with open(filename, 'w') as file:
        file.write(f"{len(qualified)}\n")
        for index, (surname, name, score) in enumerate(qualified, start=1):
            file.write(f"{index}) {name[0]}. {surname} {score}\n")

def main():
    k, participants = read_tournament_data('first_tour.txt')
    qualified = filter_and_sort_participants(k, participants)
    write_second_tour_data('second_tour.txt', qualified)

if __name__ == "__main__":
    main()
