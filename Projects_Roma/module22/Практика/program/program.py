import os


def show_menu():
    print('Введите:')
    print('\t1 - Посмотреть клиентов')
    print('\t2 - Добавить клиента')
    print('\t3 - Узнать количество клиентов в БД')
    print('\t0 - Если хотите выйти')


def show_client_table(client_dict_list):
    for entry in client_dict_list:
        print(f"| {entry['id']:>6} | {entry['name']:<10} | {entry['surname']:<15} | {entry['age']:>4} |")


def get_client_list(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        return content


def append_client(filename, client_dict):
    new_client_str = f'{client_dict["id"]};{client_dict["name"]};{client_dict["surname"]};{client_dict["age"]}'
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(new_client_str + '\n')


def input_client_dict(last_id):
    client_dict = {
        "id": str(last_id + 1),
        "name": input("Введите имя:\t"),
        "surname": input("Введите фамилию:\t"),
        "age": input("Введите возраст:\t")
    }
    return client_dict


def get_client_quantity(filename):
    content = get_client_list(filename)
    if len(content) == 0:
        return 0
    else:
        client_dict_list = parse_clients(content)
        client_quantity = len(client_dict_list)
        return client_quantity


def parse_clients(file_content):
    content_list = file_content.split('\n')
    client_dict_list = []
    for client_string in content_list:
        if client_string == '':
            continue
        client_data_list = client_string.split(';')
        client_dict = {'id': client_data_list[0],
                       'name': client_data_list[1],
                       'surname': client_data_list[2],
                       'age': client_data_list[3]}
        client_dict_list.append(client_dict)
    return client_dict_list


def main():
    filename = 'database.csv'

    clear = lambda: print('\n' * 100, end="")

    while True:
        show_menu()
        choice = input('Ваш выбор:\t')
        if choice == '0':
            clear()
            print('Вы вышли.')
            break
        elif choice == '1':
            clear()
            client_content = get_client_list(filename)
            client_dict_list = parse_clients(client_content)
            show_client_table(client_dict_list)
        elif choice == '2':
            clear()
            last_id = get_client_quantity(filename)
            client_dict = input_client_dict(last_id)
            append_client(filename, client_dict)
        elif choice == '3':
            clear()
            client_quantity = get_client_quantity(filename)
            print(f'Количество клиентов в БД = {client_quantity}')
        else:
            clear()
            print(f'Выбора "{choice}" в программе нет')


main()
