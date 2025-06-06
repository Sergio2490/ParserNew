from selenium import webdriver
from selenium.webdriver import Keys  #для ввода текста на сайте в клавиатуры
from selenium.webdriver.common.by import By  # для поиска эл-тов на странице с пом DOM
import time

browser = webdriver.Firefox()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

assert "Википедия" in browser.title  #определяем, точно ли нужная нам страница
time.sleep(5)

search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys("Солнечная система")
search_box.send_keys(Keys.RETURN)
time.sleep(5)

a = browser.find_element(By.LINK_TEXT, "Солнечная система") #в переменной a - первый найденный элемент
a.click()  # кликаем по ссылке (по элементу)
