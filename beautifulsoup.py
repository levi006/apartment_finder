import requests
from bs4 import BeautifulSoup

url_base = 'http://sfbay.craigslist.org/search/eby/apa'
params = dict(bedrooms=1, is_furnished=1)
rsp = requests.get(url_base, params=params)
# print(rsp.url)
# print(rsp.text[:500])


# import urllib
# r = urllib.urlopen('https://sfbay.craigslist.org/search/sfc/apa?query=studio&max_price=2000&availabilityMode=0').read()
soup = BeautifulSoup(rsp.text, 'html.parser')
# print type(soup)

# print soup.prettify()[0:1000000000]

# apts = soup.find_all('p', attrs={'a class': 'result-title hdrlnk'})

apts = soup.find_all('p', attrs={'class': 'row'})
print(len(apts))

# this_appt = apts[15]
# print(this_appt.prettify())