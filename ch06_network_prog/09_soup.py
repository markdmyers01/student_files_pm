"""

    09_soup.py
    Parsing HTML with BeautifulSoup.

"""
from bs4 import BeautifulSoup
import requests

html_doc = requests.get('https://www.python.org').text
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.title.text)
# print(soup.find_all('h2'))

for h2 in soup.find_all('h2'):
    print(h2.text.strip())
