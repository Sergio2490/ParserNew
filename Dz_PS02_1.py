# Задание 1: Получение данных
# 1. Импортируйте библиотеку `requests`.
# 2. Отправьте GET-запрос к открытому API (например,
#    [https://api.github.com](https://api.github.com/)) с параметром для поиска репозиториев
#    с кодом html.
# 3. Распечатайте статус-код ответа.
# 4. Распечатайте содержимое ответа в формате JSON.

import requests
import pprint

zzz={
   "q":"html"
}
url = "https://api.github.com/search/repositories"
response = requests.get(url, params=zzz)
print(response.status_code)
pprint.pprint(response.json())