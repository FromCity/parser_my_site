from bs4 import BeautifulSoup
import requests

url = 'https://recogtxt.com/'

page = requests.get(url)
print('page status:', page.status_code)


soup = BeautifulSoup(page.text, "html.parser")


p_card_title = soup.findAll('div', class_='p-card-title')
p_card_content = soup.findAll('div', class_='p-card-content')
print(p_card_title)
for data in p_card_content:
    print(data.text)
