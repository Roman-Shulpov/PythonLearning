import requests
from urllib.parse import urlparse


def download_image(url):


    response = requests.get(url)
    if response.status_code == 200:
        parsed_url = urlparse(url)
        filename = parsed_url.path.split('/')[-1]
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f'Файл {filename} успешно сохранен.')
    else:
        print('Ошибка при загрузке файла.')

# url = 'https://www.amic.ru/images/post_gallery/gallery/3396/40063/medium.jpg?_=1752364182'
url = 'http://144.91.114.139:8080/api/v1/s3-file/spot-image/bc874ae8-0607-4156-938d-a11fdf4da5b9'
download_image(url)
