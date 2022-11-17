import requests
from bs4 import BeautifulSoup

url='https://parsinger.ru/html/index3_page_1.html'
mass = []
mass_with_links_kon = []
summ = 0
response = requests.get(url=url)

response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

links = soup.find('div', class_='pagen').find_all('a')

for link in links:
    mass.append(link['href'])


for i in range(len(mass)):
    url_1 = f'https://parsinger.ru/html/{mass[i]}'
    response_1 = requests.get(url=url_1)
    response_1.encoding = 'utf-8'
    soup_1 = BeautifulSoup(response_1.text, 'lxml') #сварили суп из первой страницы

    keys = soup_1.find('div', class_='item_card').find_all('a', class_='name_item')
    for key in keys:
        mass_with_links_kon.append(key['href'])

for j in range(len(mass_with_links_kon)):
    url = f'https://parsinger.ru/html/{mass_with_links_kon[j]}'
    response_2 = requests.get(url=url)
    response_2.encoding = 'utf-8'
    soup_2 = BeautifulSoup(response_2.text, 'lxml')

    art_goods = soup_2.find('p', class_='article').text
    print(art_goods)
















