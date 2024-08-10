lastname = input("Введите фамилию получателя: ")
firstname = input("Введите имя получателя: ")
street = input("Введите адрес проживания получателя: ")
house_number = int(input("Введите номер дома получателя: "))


def info_output():
    print("Данные получателя: \n")
    print(f"Фамилия: {lastname}")
    print(f"Имя: {firstname}")
    print(f"Адрес: {street}")
    print(f"Номер дома: {house_number}")
    print()
    print()


info_output()
info_output()
info_output()
