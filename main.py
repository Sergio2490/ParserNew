import requests
import pprint
response = requests.get("https://api.github.com")
# print(response.status_code)
# if response.ok:
#     print("запрос выполнен успешно")
# else:
#     print("произошла ошибка")
# print(response.text)
print(response.text)
response_json = response.json()
pprint.pprint(response_json)
#

#dict = {
#    "url": "https://www.google.com",
#    "title": "Google"
#}