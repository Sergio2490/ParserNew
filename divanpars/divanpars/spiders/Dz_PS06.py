# Попробуй написать spider для нахождения всех источников освещения с сайта divan.ru
# Нужно взять название источника освещения, цену и ссылку
# Результаты сохраните в csv файл
import scrapy
import csv

class DzPs06Spider(scrapy.Spider):
    name = "DZ_PS06"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        svets = response.css("div._Ud0k")  #в перем-й svets - список светильников с карточками (_Ud0k - выделяется вся карточка)

        parsed_data = []

        for svet in svets:
            name = svet.css("div.lsooF span::text").get()  # :: - псевдоэлемент, берем только текст у span/ .get()- берем только 1-й элемент
            price = svet.css("div.pY3d2 span::text").get()
            url = svet.css('a').attrib["href"]

            parsed_data.append([name, price, url])

        # записываем данные в csv
        with open("svet.csv", "w", newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file, delimiter = ';')  #создаем объект writer. Русский Excel не понимает разделители ","
            writer.writerow(["Name", "Price", "Url"])
            writer.writerows(parsed_data)
