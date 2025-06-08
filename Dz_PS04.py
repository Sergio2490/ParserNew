#Д.з.
# Напишите программу, с помощью которой можно искать информацию на Википедии с помощью консоли.
# 1. Спрашивать у пользователя первоначальный запрос.
# 2. Переходить по первоначальному запросу в Википедии.
# 3. Предлагать пользователю три варианта действий:
#      1) листать параграфы текущей статьи;
#      2) перейти на одну из связанных страниц — и снова выбор из двух пунктов:
#            - листать параграфы статьи;
#            - перейти на одну из внутренних статей.
#      3) выйти из программы.

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Firefox()
browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
answer = input("Введите запрос, для поиска информаци в Википедии: ")
answer = answer.capitalize()

assert "Википедия" in browser.title  # Проверка на наличие заголовка "Википедия" в теге <title>Википедия
time.sleep(3)


# Сейчас б. искать строку ввода в Википедии  <input id = "searchInput">
search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(answer)  #в строку поиска вводим то, что ввел пользователь
search_box.send_keys(Keys.RETURN)  # переходим на страницу с результатами поисков в Википедии
time.sleep(3)

# сейчас п.3 - щелкаем на первую статью b dsdjlbv vty. bp 3-[ geyrnjd/
a = browser.find_element(By.LINK_TEXT, answer) #в переменную a - первый найденный элемент
a.click()

def second_point():
    #Если выбран Пункт 2. Перед этим юзер ввел слово, мы вывели список статей и зашли в первую (щелкнули по первой ссылке)
    #Далее мы поместим в список все Основные статьи на этой странице и перейдем в рандомную

    hatnotes = []   #список для хранения Основных статей странички
    for element in browser.find_elements(By.TAG_NAME, "div"): #мы б.перебирать список элементов с тэгами div
        cl = element.get_attribute("class")  #берем очередной элемент тэга div  и ищем у него атрибут class
        if cl == "hatnote navigation-not-searchable ts-main": #если cl (класс) hfdty "название класса", то мы вставляем этот элемент в список hatnotes[]
            hatnotes.append(element)
    #в итоге соберем список всех эл-тов с таким названием класса (Основных статей)
    #print(hatnotes)
    hatnote = random.choice(hatnotes) #в переменной- случайный элемент из списка
    link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")    #сейчас нам нужно перейти по ссылке. У нас есть тэг div, а внутри него - тэг a со ссылкой. Т.е. внутри тэга div ищем тэг a и переходим по нему
    browser.get(link)  # Мы открыли случайную Основную статью

    # выводим меню из 3-х пунктов
    user_choice1 = input("Выберите дальнейшие действия: \n1 - листать параграфы статьи (по Enter)\n2 - перейти на одну из внутренних статей")
    if user_choice1 == "1":
        paragraphs = browser.find_elements(By.TAG_NAME, "p")
        for paragraph in paragraphs:
            print(paragraph.text)
            br = input()
            if br == "3":
                exit()
    elif user_choice1 == "2":
        #Здесь нам нужно внутри уже открытой ранее(перед if) статьи перейти по пункту меню на случайную внутреннюю статью
        contents = []  #список элементов внутренних статей
        #for element in browser.find_elements(By.TAG_NAME, "div"):
        #        el = element.get_attribute("class")
        #        if el == "toctitle":
        #            contents.append(element)
        #print(f"Это список с пунктами меню: ", contents)

        contents = browser.find_elements(By.CSS_SELECTOR, "#mw-content-text a")
        random_link = random.choice(contents)
        link = random_link.get_attribute("href")
        browser.get(link)

        #Сейчас выбираем случайный элемент списка(пункт содержание)
        #content = random.choice(contents)
        #link = content.find_element(By.TAG_NAME, "a").get_attribute("href")
        #browser.get(link)
        #print(link.text)

    return


#выводим меню из 3-х пунктов
user_choice = input("Выберите дальнейшие действия: \n1 - листать параграфы текущей статьи (по Enter)\n2 - перейти на одну из связанных страниц (рандомно)\n3 - выйти из программы")
if user_choice =="1":
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        br = input()
        if br == "3":
            exit()
elif user_choice == "2":
    second_point()
elif user_choice == "3":
    exit()

