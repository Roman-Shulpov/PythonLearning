# Задача 1. Challenge-2 Что нужно сделать Вдохновившись мотивацией Антона, ваш друг тоже решил поставить перед собой
# задачу, но не напрямую связанную с математикой, а именно: написать функцию, которая выводит все числа от 1 до num
# без использования циклов. Помогите другу реализовать такую функцию.
#
# Пример работы программы
#
# Введите num: 10
#
# 1
#
# 2
#
# 3
#
# 4
#
# 5
#
# 6
#
# 7
#
# 8
#
# 9
#
# 10
<<<<<<< HEAD
=======

def dividing(num):
    if num == 1:
        return 1
    output_number = dividing(num - 1)
    print(output_number)
    return num


num_dividing = dividing(10)
print(num_dividing)
>>>>>>> 7ed4e3aade34177a88a34d01f13ba701ff6728c2
