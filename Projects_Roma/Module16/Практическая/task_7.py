people = int(input('Кол-во человек: '))
number = int(input('Какое число в считалке? '))
print(f'Значит выбывает каждый {number}-й человек')
list_people = list(range(1, people + 1))
start = 0
while len(list_people) > 0:
    print('\nТекущий круг людей: ', list_people)

print('\nОстался человек под номером', *list_people)
