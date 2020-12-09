
from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint

main_link = 'https://www.hh.ru'

vak = str(input())

params = {
    'save_area' : 'true',
    'clusters' : 'true',
    'enable_snippets' : 'true',
    'text' : f'{vak}',
    'showClusters' : 'true'
}

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

link = f'{main_link}/search/vacancy'

response = requests.get(link, params=params, headers=headers)

soup = bs(response.text,'html.parser')

if response.ok:
    vak_list = soup.findAll('div', {'class': 'vacancy-serp-item__row vacancy-serp-item__row_header'})
    vakans = []
    for vakansiy in vak_list:
        vak_data = {}
        vak_name = vakansiy.find('a')
        vak_link = vak_name.get('href')
        try:
            vak_money = vakansiy.findAll('span', {'class' : 'bloko-section-header-3 bloko-section-header-3_lite'})[-1].text
        except:
            vak_money = 0.0
        vak_data['name'] = vak_name.text
        vak_data['link'] = vak_link
        vak_data['money'] = vak_money
        vakans.append(vak_data)
pprint(vakans)
