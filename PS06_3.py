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
        title = vacancy.find_element(By.CSS_SELECTOR,  'span[data-qa="serp-item__title-text"]').text  # Имя вакансии
        company = vacancy.find_element(By.CSS_SELECTOR,  'span[data-qa="vacancy-serp__vacancy-employer-text"]').text  #Название компании
        #salary = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___pbpft_3-0-47').text
        salary = "не указана"
        try:
            salary_span = vacancy.find_element(
                By.XPATH,
                './/span[contains(@class, "magritte-text") and contains(string(.), "₽")]'
            )
            salary = salary_span.text.strip()
        except:
            pass
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_5-0-28').get_attribute('href')
    except:
        print("произошла ошибка парсинга")
        continue

    parsed_data.append([title, company, salary, link])

with open("hh.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["Название вакансии", "название компании", "зарплата", "ссылка на вакансию"])
    writer.writerows(parsed_data)





