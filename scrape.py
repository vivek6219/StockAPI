import requests
from bs4 import BeautifulSoup
req = requests.get("https://finance.yahoo.com/")

class Scrape:
    print(req)
    soup = BeautifulSoup(req.content, 'html.parser')
    print(soup.prettify)