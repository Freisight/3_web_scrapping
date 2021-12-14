from bs4 import BeautifulSoup
import requests

req = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(req.text, 'html.parser')

articles = soup.find_all('article')
filtered_info = []

DESIRED_HUBS = ['python', 'язык']

for article in articles:
    title = article.find('a', class_="tm-article-snippet__title-link").text
    title_low = title.lower()
    for to_find in DESIRED_HUBS:
        if to_find in title_low:
            list = []
            date = article.find('time').attrs.get('title')
            list.append(date)  
            list.append(title)
            href = article.find('a', class_="tm-article-snippet__title-link").attrs.get('href')
            full_href = 'https://habr.com' + href
            list.append(full_href) 
            filtered_info.append(list)

for item in filtered_info:
    print(f'Дата размещения: {item[0]}, Заголовок: "{item[1]}", URL: "{item[2]}"')