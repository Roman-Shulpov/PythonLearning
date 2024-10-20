# Задание 3. Товары
# Что нужно сделать
# В базе данных магазина вся необходимая информация по товарам делится на два словаря: первый отвечает за коды товаров,
# второй — за списки количества разнообразных товаров на складе:
#
# goods = {
# 'Лампа': '12345',
# 'Стол': '23456',
# 'Диван': '34567',
# 'Стул': '45678',
# }
# store = {
# '12345': [
# {'quantity': 27, 'price': 42},
# ],
# '23456': [
# {'quantity': 22, 'price': 510},
# {'quantity': 32, 'price': 520},
# ],
# '34567': [
# {'quantity': 2, 'price': 1200},
# {'quantity': 1, 'price': 1150},
# ],
# '45678': [
# {'quantity': 50, 'price': 100},
# {'quantity': 12, 'price': 95},
# {'quantity': 43, 'price': 97},
# ],
# }
# Каждая запись второго словаря отображает, сколько и по какой цене закупалось товаров. Цена указана за одну штуку.
#
# Напишите программу, которая рассчитывает общую стоимость позиций для каждого товара на складе и выводит эту информацию
# на экран.
#
# Результат работы программы:
#
# Лампа — 27 штук, стоимость 1134 рубля.
#
# Стол — 54 штуки, стоимость 27 860 рублей.
#
# Диван — 3 штуки, стоимость 3550 рублей.
#
# Стул — 105 штук, стоимость 10 311 рублей

def get_key_by_value(dict_value):
    founded_key = None
    for key, value in goods.items():
        if dict_value == value:
            founded_key = key
    return founded_key


goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200, 'kek': 555},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {
            'quantity': 50,
            'price': 100},
        {
            'quantity': 12,
            'price': 95},
        {
            'quantity': 43,
            'price': 97},
    ],
}

# Область всех продуктов
for key, value in store.items():
    # Область одного продукта
    total_product_sum = 0
    total_quantity = 0

    for item in value:
        # Область одной поставки
        postavka_sum = item['quantity'] * item['price']
        total_product_sum += postavka_sum
        product_quantity = item['quantity']
        total_quantity += product_quantity
    print(f"{get_key_by_value(key)} - {total_quantity} шт, стоимость {total_product_sum} рублей")


