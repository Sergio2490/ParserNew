import requests
import pprint

#созадим словарь для поиска на сайте гитхаба только репозиториев с яз.прогр python
params = {
    #'q': 'python'
    'q':'JavaScript'
}
response = requests.get("https://api.github.com/search/repositories", params = params)  #1 params - атрибут ф-ции get()? 2-й params - значение атрибута - наш словарь

#Будем выводит то, что получили
response_json = response.json()
pprint.pprint(response_json)
