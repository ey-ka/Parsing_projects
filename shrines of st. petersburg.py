from bs4 import BeautifulSoup
import requests

svyat_list = []

for i in range(1, 25):
    url = f'http://www.encspb.ru/object/2804687243/D_1803401815/{i}?lc=ru'
    print(url)

    site = requests.get(url)
    rec = site.text

    soup = BeautifulSoup(rec, features='html.parser')
    svyats = soup.find_all('div', class_='artName')

    for svyat in svyats:
        svyat_list.append(svyat.text)

with open('svyat.txt', 'a', encoding='utf-8') as file:
    for line in svyat_list:
        file.write(f'{line}\n')
