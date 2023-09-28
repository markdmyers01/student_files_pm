"""

    10_requests_and_soup.py
    Using both requests and BeautifulSoup to retrieve and parse HTML.

"""
from bs4 import BeautifulSoup     # pip install beautifulsoup4
import requests                   # pip install requests

content = requests.get('https://cisco.com').text

soup = BeautifulSoup(content, 'html.parser')
print(soup.title.text)

print('-----')
print('h2\'s on the page:')
for elem in soup.find_all('h2'):
    print(elem.text)

print('-----')
# Note: due to the dynamic nature of live webpages, the selector below can
#       change.  If this line generates an error, you should follow steps discussed
#       in the slides for using browser dev tools to identify and correct the selector
#       (as of this writing, the following selector works
selector = '#cdc-homepage-hero h1'
headline = soup.select(selector)                # select() accepts CSS selectors
if headline:
    print(headline[0].text)                     # Use .strip() to remove whitespace
