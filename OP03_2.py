import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"

response = requests.get(url)  #отправляем Get-запрос
html = response.text  #получаем html код странички, сохр его в перем.html и далее - с этим кодом работаем
soup = BeautifulSoup(html, "html.parser")


