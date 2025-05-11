#post запрос
import requests

url = "https://jsonplaceholder.typicode.com/posts"

data1 = {
    "title": "тестовый post запрос",
    "body": "тестовый контент post запроса",
    "userId": 2
}

response = requests.post(url, data=data1)  #data-параметры, data1-инф-ция, к-я б передана в кач-ве параметров

print(response.status_code)

print(f"ответ - {response.json()}")  #тело ответа


