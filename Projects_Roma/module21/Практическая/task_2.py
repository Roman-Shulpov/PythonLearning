# Задача 2. Поиск элемента — 2 Что нужно сделать Пользователь вводит искомый ключ. Если он хочет, то может ввести
# максимальную глубину — уровень, до которого будет просматриваться структура.
#
# Напишите функцию, которая находит заданный пользователем ключ в словаре и выдаёт значение этого ключа на экран. По
# умолчанию уровень не задан. В качестве примера можно использовать такой словарь:
#
site = \
    {
        'html': {
            'head': {
                'title': 'Мой сайт'
            },
            'body': {
                'h2': 'Здесь будет мой заголовок',
                'div': 'Тут, наверное, какой-то блок',
                'p': 'А вот здесь новый абзац'
            }
        },
    }

def recursive_print(request_1, level):
    if isinstance(request_1, dict):
        print(request_1)
        for key, value in request_1.items():
            recursive_print(value, level + 1)
    else:
        recursive_print(request_1, level)

request_1 = input("Введите искомый ключ: ").lower()
depth_request = input("Хотите ввести максимальную глубину? Y/N: ").lower()
if depth_request == 'n':
    for key, value in site.items():
        print(value[request_1])
elif depth_request == 'y':
    level = int(input("Введите максимальную глубину: "))
    recursive_print(request_1, level)



    
    


# ВЫВОД ВСЕГО:


# ВЫВОД ВСЕГО:

# Пример 1
#
# Введите искомый ключ: head
#
# Хотите ввести максимальную глубину? Y/N: n
#
# Значение ключа: {'title': 'Мой сайт'}
#
# Пример 2
#
# Введите искомый ключ: head
#
# Хотите ввести максимальную глубину? Y/N: y
#
# Введите максимальную глубину: 1
#
# Значение ключа: None


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key_in_dict(data_dict, search_key, max_depth, current_depth=0):
    if current_depth >= max_depth:  # Изменить условие на >=
        return None

    if search_key in data_dict:
        return data_dict[search_key]

    for key, value in data_dict.items():
        if isinstance(value, dict):
            result = find_key_in_dict(value, search_key, max_depth, current_depth + 1)
            if result is not None:
                return result

    return None


user_key = input("Введите искомый ключ: ").lower()
depth_prompt = input("Хотите ввести максимальную глубину? Y/N: ").lower()

if depth_prompt == 'n':
    max_depth = float('inf')
else:
    max_depth = int(input("Введите максимальную глубину: "))

found_value = find_key_in_dict(site, user_key, max_depth)

if found_value is not None:
    print(f"Значение ключа: {found_value}")
else:
    print("Ключ не найден.")
