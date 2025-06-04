from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Firefox()
browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

hatnotes = []

for element in browser.find_elements(By.TAG_NAME, "div"): # мы б. перебирать список получившихся эл-тов с тэгом "div"
    cl = element.get_attribute("class") #берем конкр-й эл-нт тэга div и ищем у него атрибут class. Если он есть, проверяем еще:
    if cl == "hatnote navigation-not-searchable ts-main": # если cl(класс) б равен "названию класса", добавляем этот эл-нт в список
        hatnotes.append(element)

print(hatnotes)
hatnote = random.choice(hatnotes)

link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href") #внутри тэга а берем атрибут href.то, что хранится в href запишется в перем-ю link
browser.get(link)  # И мы м по этому link перейти к рандомной статье


