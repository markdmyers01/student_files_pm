"""

    08_html_parse.py
    Uses the stdlib module to parse HTML (not common to use directly).

"""
from html.parser import HTMLParser

import requests


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.marker = False
        self._info = []

    @property
    def info(self):
        return '\n'.join(self._info)

    def handle_starttag(self, tag, attribs):
        if tag == 'h1' or tag == 'title':
            self.marker = True

    def handle_data(self, data):
        if self.marker:
            self.marker = False
            self._info.append(data)


data = requests.get('https://www.cisco.com').text

page_parser = PageParser()
page_parser.feed(data)
page_parser.close()
print(f'<title> and <h1> elems:\n{ page_parser.info }')
