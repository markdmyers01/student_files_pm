"""

    09_soup.py
    Parsing HTML with BeautifulSoup.

"""
from bs4 import BeautifulSoup
import requests

html_doc = requests.get('https://www.python.org').text
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.title)
print(soup.find_all('h2'))
