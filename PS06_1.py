# Видео 1 - 1) Очистка данных (в таблице от пробелов)
import requests
from bs4 import BeautifulSoup

url = "https://"

response = requests.get(url)
soup = BaseException(response.text, "html.parser")

rows = soup.find_all("tr") # коллекция, в которой все строки (ряды)
data = []

for row in rows:
    cols = row.find_all("td") # cols - еще одна коллекция,в которой нах все Ячейки, содержащиеся в текущем ряду(строке)
    cleaned_cols = [col.text.strip() for col in cols] #сокращ запись цикла for. Перебираем в цикле наш список
                                          # ячеек(колонок) cols. Каждая текущая колонка сохр-ся в перем. col, затем мы
                                           #получаем текст из этой колонки (col.text) и очищаем его от пробелов с обеих сторон
    data.append(cleaned_cols)
print(data)
