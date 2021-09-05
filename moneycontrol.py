import datetime
import json

from bs4 import BeautifulSoup
import requests

url = "https://moneycontrol.com"
keywords = ['jhun', 'taliban', 'bitcoin', 'elss', 'gold']

print("\n ======================= {} =========================== \n".format(url))

r = requests.get(url)
soup = BeautifulSoup(r.content, "html5lib")
articles = {}

for href in soup.find_all('a'):
    # print(href.attrs.get('title'))
    for keyword in keywords:
        if href.attrs.get('title') is not None and keyword.lower() in href.attrs.get('title').lower():
            # print("title - {} \n link - {}".format(href.attrs.get('title'), href.attrs.get('href')))
            articles[href.attrs.get('title')] = href.attrs.get('href')

for title in articles.keys():
    print("title - {} \n link - {}".format(title, articles[title]))

filename = str(datetime.datetime.now().date()) + "_moneycontrol.txt"
with open(filename, 'w') as f:
    for key, value in articles.items():
        f.write("\n * {} - {} \n".format(key, value))

