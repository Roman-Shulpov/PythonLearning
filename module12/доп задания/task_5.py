sphere_radius = int(input("Введите радиус сферы: "))
pi = float(3.14)

sphere_area = 4 * pi * sphere_radius ** 2

sphereVolume = 4 / 3 * pi * sphere_radius ** 3


select_operation = int(input("Что найдём? : 1 - площадь сферы, 2 - объём шара."))
if select_operation == 1:
    print("Площадь сферы равна: ", sphere_area)
elif select_operation == 2:
    print("Объём шара равен: ", sphereVolume)
else:
    print("error!")
