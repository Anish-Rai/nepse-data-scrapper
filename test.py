import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
def gainer_loser():
    new_list =[]
    indexs = ['losers', 'gainers']
    url = 'https://nepalstockinfo.com/'
    urls = [url + index for index in indexs]
    for i, url in enumerate(urls):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find('tbody').find_all('tr')[2:17]
        title = ['symbol', 'LTP', '% change','status']
        date = soup.find('td', colspan=3).text.strip()[5:]
        body = []
        for d in data:
            body.append(d.text.strip().split(' '))
        new_list += [b+[indexs[i]]for b in body]
    df = pd.DataFrame(data=new_list, columns=title, )
    return df.to_json(orient='records')














