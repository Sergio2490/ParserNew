import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"

response = requests.get(url)  #отправляем Get-запрос
html = response.text  #получаем html код странички, сохр его в перем.html и далее - с этим кодом работаем
soup = BeautifulSoup(html, "html.parser")

text = soup.find_all("span", class_ ="text")
#print(text)
author = soup.find_all("small", class_ ="author")
#print(author)

for i in range(len(text)):
    print(f"Цитата номер - {i+1}")
    print(text[i].text)
    print(f"Автор цитаты - {author[i].text}\n")
