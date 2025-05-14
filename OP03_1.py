from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com/"

response = requests.get(url)
#print(response.content)  - просто проверили

html = response.text

soup = BeautifulSoup(html, "html.parser")
links = soup.find_all("a")  #ищем все ссылки на сайте
#print(links) #неудобно, в одну строку всё

for link in links:
    print(link.get("href"))


