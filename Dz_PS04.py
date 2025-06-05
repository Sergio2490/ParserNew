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

#выводим меню из 3-х пунктов
user_choice = input("Выберите дальнейшие действия: \n1 - листать параграфы текущей статьи (по Enter)\n2 - перейти на одну из связанных страниц (рандомно)\n3 - выйти из программы")
if user_choice =="1":
    pass
elif user_choice == "2":
    pass
elif user_choice == "3":
    browser.quit()
