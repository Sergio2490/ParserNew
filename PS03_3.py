#video_3
import requests
from bs4 import BeautifulSoup

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
       # print(response.text)

        soup = BeautifulSoup(response.content, "html.parser") #создали объект soup и передали в него весь контент сайта
        english_words = soup.find("div", id="random_word").text.strip() #нашли все div с атрибутом id="random_word"
        word_definition = soup.find("div", id="random_word_definition").text.strip()

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
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        print(f"Значение слова - {word_definition}")  #вывели описание слова
        user = input("Что это за слово? ")
        if user == word:
            print("Ответ верный")
        else:
            print(f"Ответ неверный. Было загадано это слово - {word}")

        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again != "y":
            print("Спасибо за игру")
            break  #выходим из цикла, завершаем программу

word_game()





