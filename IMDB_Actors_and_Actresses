from bs4 import BeautifulSoup
import requests
import lxml

names_list = []

for i in range(1, 9990000): 
    url = f'https://www.imdb.com/name/nm000000{i}'
    print(url)

    site = requests.get(url)
    rec = site.text

    soup = BeautifulSoup(rec,'lxml')
    names = soup.find('span', class_='itemprop')



    for name in names:
        names_list.append(name)

with open('names.txt', 'a', encoding='utf-8') as file:
    for line in names_list:
        file.write(f'{line}\n')
