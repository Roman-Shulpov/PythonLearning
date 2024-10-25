# Решение задачи 4
# Полный код решения задачи:

def check_ip(ip_address):
    split_ip_address = ip_address.split(".")
    if len(split_ip_address) == 4:
        for part_ip_address in split_ip_address:
            if not part_ip_address.isdigit():
                print(f'\tОшибка: {part_ip_address} не целое число.')
                break
            elif not int(part_ip_address) <= 255:
                print(f'\tОшибка: {part_ip_address} превышает 255.')
                break
        else:
            print('\tIP-адрес корректен')
            return ip_address
    else:
        print('Ошибка: адрес — это четыре числа, разделённые точками.')

def check_file_name(file_name):
    incorrect_endings = '.txt', '.docx'
    special_symbols = '@', '№', '$', '%', '^', '&', '*', '(', ')', '\\'

    if file_name.startswith(special_symbols):
        print('\tОшибка: название начинается на один из специальных символов')
    elif not file_name.endswith(incorrect_endings):
        print('\tОшибка: неверное расширение файла. Ожидалось .txt или .docx')
    else:
        print('\tФайл назван верно.')
        return file_name

def maximum_length(text):
    text = text[0].split()
    return max(text, key=len)

data = [
    ["128.16.35.a4", ["file_21.txt @data_report.txt notes2024.txt"]],
    ["34.56.42,5", ["file.txt analysis_results.ttx notes2000.txt"]],
    ["128.0.0.255", ["file_1.txt document_2024.docx notes2022.txt"]],
    ["240.127.56.340", ["file_432.txt ^budget_summary.txt notes2021.txt"]],
    ["192.168.1.10", ["file_432.txt  important_info.txt notes1900.txt"]],
    ["192.c8.1.10", ["file_432.txt  &meeting_notes.docx notes1995.txt"]],
    ["10.20.30.40", ["file_432.txt  analysis_results.txt notes1998.txt"]],
]

valid_info = []
for info in data:
    print(f"Проверяю ip {info[0]}")
    ip_address = check_ip(info[0])

    print(f"Ищу самый длинный файл для ip {info[0]}")
    maxi_length = maximum_length(info[1])

    print(f"\tЭто файл {maxi_length}. \nПроверяю корректность имени")
    file_name = check_file_name(maxi_length)

    if ip_address and file_name:
        valid_info.append([ip_address, info[1]])
    print("=" * 50)

print(f"Новая структура данных\n[")
for i in valid_info:
    print(f"\t{i}")
print("]")