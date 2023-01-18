
from bs4 import BeautifulSoup
import requests



def futb(url):
    headers = {  

        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46"

    }
    req = requests.get(url, headers)

    names_list = []
    names_list_it = []

    letter_list = ("abc")
    sec_list = ("abc")

    for x in letter_list:
        for y in sec_list:
            url = f'https://fbref.com/en/players/{x}{y}/'
            name = (url)
            names_list.append(name)

            print(url)


        site = requests.get(url)
        rec = site.text

        soup = BeautifulSoup(rec, 'html.parser')
        

        for name in names_list:

            rec2 = requests.get(name, headers)
            rect = rec2.text
            soup = BeautifulSoup(rect, 'html.parser')
            infon = soup.select('.section_content > p')    
            name_it = infon
            for item in name_it:
                names_list_it.append(item.text)






    with open("names.txt", "a", encoding='utf-8') as file:
        for line in names_list_it:

            file.write(f'{line}\n')


futb("https://fbref.com/en/players/")
