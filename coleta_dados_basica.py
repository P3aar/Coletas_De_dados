import pandas
import requests
from bs4 import BeautifulSoup

print('Request: ')
response = requests.get('https://webscraper.io/test-sites/tables/tables-semantically-correct')
print(response.text[:600])

print('BeatifulSoup: ')
soup = BeautifulSoup(response.text,'html.parser')
print(soup.prettify()[:1000])

print('pandas: ')
url_dados = pandas.read_html('https://webscraper.io/test-sites/tables/tables-semantically-correct')
print(url_dados[0].head(20))

