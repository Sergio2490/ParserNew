#video_3
import requests
from bs4 import BeautifulSoup

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        print(response.text)

        soup = BeautifulSoup(response.content, "html.parser") #создали объект soup и передали в него весь контент сайта
        english_words = soup.find_all("div", id="random_word") #нашли все div с атрибутом id="random_word"
        word_definition = soup.find_all("div", id="random_word_definition")

        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print("Произошла ошибка")  #это ф-ция 1, к-я получает данные с сайта

def word_game(): #Нам б. выводиться описание слова. А мы д. ввести само слово. Если верно - вывод Угадали, нет - Не угадали
    print("Добро пожаловать в игру")
    while True:  #бесконечный цикл
        word_dict = get_english_words()  #получили весь словарь с данными






