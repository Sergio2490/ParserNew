# Задание 3: Отправка данных
# 1. Используйте API, которое принимает POST-запросы для создания новых данных (например,
#     https://jsonplaceholder.typicode.com/posts).
# 2. Создайте словарь с данными для отправки (например, `{'title': 'foo', 'body': 'bar', 'userId': 1}`).
# 3. Отправьте POST-запрос с этими данными.
# 4. Распечатайте статус-код и содержимое ответа.

import requests
import pprint

dict = {
    "title": "foo",
    "body": "bar",
    "userID": 1
}
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.post(url, data=dict)
print(response.status_code)
pprint.pprint(response.json())