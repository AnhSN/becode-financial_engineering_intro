import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0'}
allstocks = []
#allstocks = ['AAPL', 'YOU']
stockdata = []

'''
    getData(symbol) function
    Will gather the data from the input page.
    The data is gonna be saved in stockdata with the for loop.
'''
def getData(symbol):
    url = f'https://finance.yahoo.com/quote/{symbol}'
    r = requests.get(url, headers=headers)

    # check if connexion is made
    #print(r.status_code)

    soup = BeautifulSoup(r.text, 'html.parser')
    stock = {
        'symbol' : symbol,
        'price' : soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
        'change' : soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('span')[0].text,
        'percentage' : soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('span')[1].text,
    }
    return stock

for symbol in allstocks:
    stockdata.append(getData(symbol))

print(stockdata)