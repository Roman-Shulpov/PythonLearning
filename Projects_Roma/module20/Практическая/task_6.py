# Задача 6. Контакты — 3 Что нужно сделать Мы уже помогали Степану с реализацией телефонной книги на устройстве,
# однако внезапно оказалось, что ей не хватает ещё одной полезной функции — поиска.
#
# Напишите программу, которая бесконечно запрашивает у пользователя действие, которое он хочет совершить: добавить
# контакт или найти человека в списке контактов по фамилии.
#
# Действие «добавить контакт»: программа запрашивает имя и фамилию контакта, затем номер телефона, добавляет их в
# словарь и выводит на экран текущий словарь контактов. Если этот человек уже есть в словаре, то выводится
# соответствующее сообщение.
#
# Действие «поиск человека по фамилии»: программа запрашивает фамилию и выводит все контакты с такой фамилией и их
# номера телефонов. Поиск не должен зависеть от регистра символов.
#
# Пример работы программы:
#
# Введите номер действия:
#
# Добавить контакт.
# Найти человека.
# При выборе действия 1:
#
# Введите имя и фамилию нового контакта (через пробел): Иван Сидоров
#
# Введите номер телефона: 888
#
# Текущий словарь контактов: {('Иван', 'Сидоров'): 888}
#
# Введите номер действия:
#
# Добавить контакт
# Найти человека
# При выборе действия 1:
#
# Введите имя и фамилию нового контакта (через пробел): Иван Сидоров
#
# Такой человек уже есть в контактах.
#
# Текущий словарь контактов: {('Иван', 'Сидоров'): 888}
#
# Введите номер действия:
#
# Добавить контакт
# Найти человека
# При выборе действия 1:
#
# Введите имя и фамилию нового контакта (через пробел): Алиса Петрова
#
# Введите номер телефона: 999
#
# Текущий словарь контактов: {('Иван', 'Сидоров'): 888, ('Алиса', 'Петрова'): 999}
#
# Введите номер действия:
#
# Добавить контакт
# Найти человека
# При выборе действия 2:
#
# Введите фамилию для поиска: Сидоров
#
# Иван Сидоров 888
#
# Введите номер действия:
#
# Добавить контакт
# Найти человека
# …….
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Основной функционал (действия) описан в отдельных функциях.
# Переменные и функции имеют значимые имена, не только a, b, c, d.
