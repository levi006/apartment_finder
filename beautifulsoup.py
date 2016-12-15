import requests
import pandas as pd
from bs4 import BeautifulSoup

url_base = 'http://sfbay.craigslist.org/search/sfc/apa'
params = dict(query='studio', max_price=2000, availabilityMode=0)
rsp = requests.get(url_base, params=params)
# print(rsp.url)
# print(rsp.text[:500])

soup = BeautifulSoup(rsp.text, 'html.parser')
# print type(soup)

apts = soup.find_all('li', attrs={'class': 'result-row'})
# print(len(apts))

this_apt = apts[5]
# print "**************"
# print(this_apt.prettify())
# print "**************"


this_time = this_apt.find('time')['datetime']
this_time = pd.to_datetime(this_time)
title = this_apt.find('a', attrs={'class': 'hdrlnk'}).text
# price = this_apt.findAll('span', attrs={'class': 'result-price'})
this_price = this_apt.find('span', {'class': 'result-price'}).text
# print type(this_price)
print(title, this_price)