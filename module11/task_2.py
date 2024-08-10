height = float(input('Введите ваш рост: '))
weight = float(input('Введите ваш вес: '))
bmi = round(weight / height ** 2, 2)
print('Ваш индекс массы тела: ', bmi)

if bmi < 18.5:
    print('У вас недостаточная масса тела.')
elif bmi < 25:
    print('У вас нормальная масса тела.')
elif bmi < 30:
    print('У вас избыточная масса тела.')
else:
    print('У вас ожирение!!!')

