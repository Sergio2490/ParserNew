from selenium import webdriver
from selenium.webdriver import Keys  #для ввода текста на сайте в клавиатуры
from selenium.webdriver.common.by import By  # для поиска эл-тов на странице с пом DOM
import time

browser = webdriver.Firefox()  # далее вставим ссылку на страницу сразу с Солнечной системой
browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

paragraphs = browser.find_elements(By.TAG_NAME, "p") #ищем ВСЕ элементы с тэгом <p> на страничке
for paragraph in paragraphs:
    print(paragraph.text) # выводим текст очередного параграфа
    input() # пучтой инпут - по нажатии Enter выводим  текст из следующего параграфа

