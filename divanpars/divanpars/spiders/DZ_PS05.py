# Попробуй написать spider для нахождения всех источников освещения с сайта divan.ru
# Нужно взять название источника освещения, цену и ссылку
import scrapy


class DzPs05Spider(scrapy.Spider):
    name = "DZ_PS05"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        svets = response.css("div._Ud0k")  #в перем-й svets - список светильников с карточками (_Ud0k - выделяется вся карточка)
        for svet in svets:
            yield {
                "name": svet.css("div.lsooF span::text").get(),  # :: - псевдоэлемент, берем только текст у span/ .get()- берем только 1-й элемент
                "price": svet.css("div.pY3d2 span::text").get(),
                "url": svet.css('a').attrib["href"]
            }

        print(f"ВСЕГО СВЕТИЛЬНИКОВ НА СТРАНИЦЕ - {len(svets)}")


