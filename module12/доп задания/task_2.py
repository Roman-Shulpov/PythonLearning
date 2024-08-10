def general_output_function():
    a = int(input())

    b = int(input())

    print("Всего", a + b, "шт.")


for n in range(3):
    print("Сколько мешков рыбы и мяса? : ")

    general_output_function()

    print("Сколько буханок белого и чёрного хлеба? : ")

    general_output_function()

    print("Сколько вёдер воды и молока? : ")

    general_output_function()
