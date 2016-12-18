import requests
import pandas as pd
import numpy as np
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

this_apt = apts[0]
# print "**************"
# print(this_apt.prettify())
# print "**************"

this_time = this_apt.find('time')['datetime']
this_time = pd.to_datetime(this_time)
this_title = this_apt.find('a', attrs={'class': 'hdrlnk'}).text
this_price = this_apt.find('span', {'class': 'result-price'}).text
# print type(this_price)
# print(title, this_price)

print('\n'.join([str(i) for i in [this_time, this_price, this_title]]))

def find_prices(results):
    prices = []
    for rw in results:
        price = rw.find('span', {'class': 'price'})
        if price is not None:
            price = float(price.text.strip('$'))
        else:
            price = np.nan
        prices.append(price)
    return prices

def find_times(results):
    times = []
    for rw in apts:
        if time is not None:
            time = time['datetime']
            time = pd.to_datetime(time)
        else:
            time = np.nan
        times.append(time)
    return times

# Now loop through all of this and store the results
results = []  # We'll store the data here

loc_prefixes = ['sfc']
# Careful with this...too many queries == your IP gets banned temporarily
search_indices = np.arange(0, 300, 100)

for loc in loc_prefixes:
	print loc

	for i in search_indices:
	    url = 'http://sfbay.craigslist.org/search/sfc/apa'.format()
	    resp = requests.get(url, params={'bedrooms': 1, 's': 10})
	    txt = BeautifulSoup(resp.text, 'html.parser')
	    apts = txt.findAll(attrs={'class': "row"})
	    
	    # Find the size of all entries
	    size_text = [rw.findAll(attrs={'class': 'housing'})[0].text
	                 for rw in apts]
	    sizes_brs = [find_size_and_brs(stxt) for stxt in size_text]
	    # sizes, n_brs = zip(*sizes_brs)  # This unzips into 2 vectors
	 
	    # Find the title and link
	    title = [rw.find('a', attrs={'class': 'hdrlnk'}).text
	                  for rw in apts]
	    links = [rw.find('a', attrs={'class': 'hdrlnk'})['href']
	             for rw in apts]
	    
	    # Find the time
	    time = [pd.to_datetime(rw.find('time')['datetime']) for rw in apts]
	    price = find_prices(apts)
	    
	    # We'll create a dataframe to store all the data
	    data = np.array([time, price, title, links])
	    col_names = ['time', 'price', 'title', 'link']
	    df = pd.DataFrame(data.T, columns=col_names)
	    df = df.set_index('time')
	    
	    # Add the location variable to all entries
	    df['loc'] = loc
	    results.append(df)
	    print data 
	        
	# Finally, concatenate all the results
	results = pd.concat(results, axis=0)

	print results.head()


