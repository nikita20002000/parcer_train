import requests
from bs4 import BeautifulSoup

url='https://parsinger.ru/html/index3_page_1.html'
mass_pages = []
mass_prod = []
mass_with_links_kon = []
summ = 0
summ_mouse = 0
response = requests.get(url=url)

response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

links_pages = soup.find('div', class_='pagen').find_all('a')
links_products = soup.find('div', class_='nav_menu').find_all('a')

for link in links_pages:
    mass_pages.append(link['href'][7::])         #собираем кол-во ссылок для перехода по вкладкам
print(mass_pages)
for link_prod in links_products:
    mass_prod.append(link_prod['href'][0:6])     #собираем кол-во ссылок для перехода по разным товарам

print(mass_prod)


for j in range(len(mass_prod)):
    for i in range(len(mass_pages)):
        url_1 = f'https://parsinger.ru/html/{mass_prod[j]}_{mass_pages[i]}'

        responce_1 = requests.get(url=url_1)
        responce_1.encodings = 'utf-8'
        soup_1 = BeautifulSoup(responce_1.text, 'lxml')

        keys = soup_1.find('div', class_='item_card').find_all('a', class_='name_item')

        for key in keys:
            mass_with_links_kon.append(key['href'])
print(mass_with_links_kon)


for k in range(len(mass_with_links_kon)):
    url_2 = f'https://parsinger.ru/html/{mass_with_links_kon[k]}'
    response_2 = requests.get(url=url_2)
    response_2.encoding = 'utf-8'
    soup_2 = BeautifulSoup(response_2.text, 'lxml')

    count_nal = soup_2.find('span', id='in_stock').text
    count_price = soup_2.find('span', id='price').text

    summ_mouse += (int(count_nal.split()[-1]) * int(count_price.split()[0]))

print(summ_mouse)























