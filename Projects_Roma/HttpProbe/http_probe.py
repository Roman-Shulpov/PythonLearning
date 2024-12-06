import requests

# Выполняем GET-запрос
response = requests.get("http://144.91.114.139:8080/api/v1/spot/all")

# Выводим статус-код ответа
print(f"Status code: {response.status_code}")

# Выводим текст ответа
print("Response text:")
print(response.text)

