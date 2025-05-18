import re
from bs4 import BeautifulSoup
import requests

# Получаем HTML-код страницы
url = "https://минюст43.рф"  # Замените на нужный URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Регулярное выражение для поиска адресов электронной почты
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Используем find_all() для поиска всех текстов, соответствующих шаблону
text_elements = soup.find_all(string=re.compile(email_pattern))

# Сохраняем найденные email в набор для удаления дубликатов
emails = set()

# Извлекаем адреса электронной почты из найденных текстовых элементов
for element in text_elements:
    found_emails = re.findall(email_pattern, element)
    emails.update(found_emails)

# Выводим найденные email
for email in emails:
    print(email)