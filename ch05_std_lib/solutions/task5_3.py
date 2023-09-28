"""

      task5_3.py    -   Consuming XML (Solution)
      Note: if internet access is not available,
      change line 39 to tree = parse_feed(feed, True)

"""
from collections import namedtuple
from datetime import datetime
import sys
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError

import requests

fields = ['title', 'description', 'pubDate']
Item = namedtuple('Item', fields)


def parse_feed(feed='', use_archived=False):
    try:
        if use_archived:
            tree = ET.parse('archived.xml')
        else:
            tree = ET.fromstring(feed)
    except ParseError as err:
        print(f'Parse error: {err}', file=sys.stderr)
        sys.exit(42)
    return tree


feed_url = 'http://rssfeeds.usatoday.com/usatodaycomnation-topstories&x=1'

try:
    feed = requests.get(feed_url).text
except requests.exceptions.RequestException:
    feed = ''

tree = parse_feed(feed)

items = []
for item in tree.findall('.//item'):
    title = item.find('.//title').text
    description_full = item.find('.//description').text
    description = description_full.split('<')[0]
    pub_date_str = item.find('.//pubDate').text
    pubDate = datetime.strptime(pub_date_str, '%a, %d %b %Y %H:%M:%S %z')
    items.append(Item(title, description, pubDate))

for item in items:
    print(f'{item.title} \n   {item.description[:70]}... \n   {item.pubDate.strftime("%b %d, %Y")}')
