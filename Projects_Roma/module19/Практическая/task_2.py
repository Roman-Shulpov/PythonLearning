# Задание 2. Криптовалюта
# Что нужно сделать
# При работе с API (application programming interface) сайта биржи по криптовалюте вы получили такие данные в виде
# словаря:
#
# data = {

# "address": "0x544444444444",

# "ETH": {
# "balance": 444,
# "totalIn": 444,
# "totalOut": 4
# },

# "count_txs": 2,

# "tokens": [
# {
# "fst_token_info": {
# "address": "0x44444",
# "name": "fdf",
# "decimals": 0,
# "symbol": "dsfdsf",
# "total_supply": "3228562189",
# "owner": "0x44444",
# "last_updated": 1519022607901,
# "issuances_count": 0,
# "holders_count": 137528,
# "price": False
# },
# "balance": 5000,
# "totalIn": 0,
# "total_out": 0
# },

# "sec_token_info": {

# "address": "0x44444",
# "name": "ggg",
# "decimals": "2",
# "symbol": "fff",
# "total_supply": "250000000000",
# "owner": "0x44444",
# "last_updated": 1520452201,
# "issuances_count": 0,
# "holders_count": 20707,
# "price": False

# },

# "balance": 500,
# "totalIn": 0,
# "total_out": 0

# }
# ]
# }

# Теперь необходимо обработать эти данные.
#
# Напишите программу, которая выполняет следующий алгоритм действий:
#
# Вывести списки ключей и значений словаря.
# В ETH добавить ключ total_diff со значением 100.
# Внутри fst_token_info значение ключа name поменять с fdf на doge.
# Удалить total_out из словарей внутри списка tokens и присвоить сумму этих значений в total_out внутри ETH.
# Внутри sec_token_info изменить название ключа price на total_price.
# После выполнения алгоритма выводить результат (словарь) не нужно.
#
# Советы и рекомендации
# Если вы достали из словаря список по ключу, то можете применять к нему методы списка.
# Например:
#
# словарь[“список”].append(123)
#
# Python возьмёт из словаря объект по ключу «список» и применит к нему метод append. Эта же логика работает с
#
# другими типами данных. Например, если вы достали из словаря словарь, то к нему можно применять методы словаря
# а если достали строку — методы строк.
#
# Чтобы не запутаться, распечатывайте объект, который получаете в данный момент. Также можно распечатать тип объекта:
# print(data)
# print(data[‘ключ’], type(data[‘ключ’]))
# print(data[‘ключ’][0], type(data[‘ключ’][0]))
#

# print(data)
# print(data[‘ключ’], type(data[‘ключ’]))
# print(data[‘ключ’][0], type(data[‘ключ’][0]))

data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

print("Ключи и значения словаря:")
for key, value in data.items():
    print(f"{key}: {value}")

data["ETH"]["total_diff"] = 100

data["tokens"][0]["fst_token_info"]["name"] = "doge"

total_out_sum = 0
for token in data["tokens"]:
    if "total_out" in token:
        total_out_sum += token["total_out"]
        del token["total_out"]

data["ETH"]["totalOut"] = total_out_sum

data["tokens"][1]["sec_token_info"]["total_price"] = data["tokens"][1]["sec_token_info"].pop("price")

