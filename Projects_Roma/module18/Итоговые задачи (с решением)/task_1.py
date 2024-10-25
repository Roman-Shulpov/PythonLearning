# Решение задачи 1
# Для решения этой задачи необходимо написать функцию, которая:
#
# принимает строку;
# разделяет её по символу «;» методом split;
# объединяет значения через запятую и пробел методом join;
# приводит каждое слово к заглавной букве, используя метод title.

def nice_view(text):
    text = " | ".join(text.split(','))
    return text.title()


site_menu = input('Введите доступное меню: ')
print('Доступное меню:', site_menu)
print('На данный момент в меню есть:', nice_view(site_menu))


