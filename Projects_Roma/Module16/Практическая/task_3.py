shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000],
        ['шатун', 200], ['седло', 2700]]

part = input('Введите запчасть: ')
part_count = 0
price = 0

for i in shop:
    if i[0] == part:
        part_count += 1
        price += i[1]
print(f"Кол-во: {part_count} \n Сумма: {price}")
