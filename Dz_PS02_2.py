# Задание 2: Параметры запроса
# 1. Используйте API, который позволяет фильтрацию данных через URL-параметры (например,
#     https://jsonplaceholder.typicode.com/posts).
# 2. Отправьте GET-запрос с параметром `userId`, равным `1`.
# 3. Распечатайте полученные записи.

import requests
import pprint

params = {
    "userId": "1"
}
url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url, params=params)

pprint.pprint(response.json())