print('Задача 1. Я стал новым пиратом!')

# Старому капитану нужно пополнить команду, но на корабль попадут только достойные! Он отобрал десять человек.
# Те, кто крикнет слово «Карамба», попадут на борт.

# Что нужно сделать

# Пользователь вводит десять слов. Напишите программу, которая определяет, сколько из них совпадают со словом «Карамба».

karamba_people = 0
for n in range(10):
    word = input("Крикни слово, чтобы попасть на борт!")
    if word == "карамба" or word == "Карамба":
        karamba_people += 1
print(f"{karamba_people} человек крикнули слово 'Карамба' и попали на борт!")

