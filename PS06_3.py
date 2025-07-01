# Разработка программы - парсера. мы б. парсить данные с hh.ru и сохранять их в csv-файл
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox() # для начала работы нам нюсоздать браузер (инициализировать его)

url = "https://tomsk.hh.ru/vacancies/programmist"  # страничка, на которой будем искать
driver.get(url)  # откроем эту страницу
time.sleep(3)  #страница открывается и надо подождать 3 сек

vacancies = driver.find_elements(By.CLASS_NAME, "vacancy-card--n77Dj8TY8VIUF0yM")  #сохр в переменную карточки всех найденных вакансий

parsed_data = []  # далее б сохр все в этом списке

for vacancy in vacancies:  #каждая отдел вакансия - in Коллекция карточек вакансий
    try:   #б ловить ошибки, если будут
        
