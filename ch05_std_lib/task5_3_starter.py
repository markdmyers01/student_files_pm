"""

      task5_3_starter.py    -   Consuming XML (starter)

      This exercise parses live XML retrieved from an API. If internet
      access is not available, change line 40 to tree = parse_feed(use_archived=True)

"""
from collections import namedtuple
from datetime import datetime
import sys
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError

import requests
import fontstyle

fields = ['title', 'description', 'pubDate']
Item = namedtuple('Item', fields)


def parse_feed(feed='', use_archived=True):
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
    descriptionFull = item.find('.//description').text
    description = descriptionFull.split('<')[0]
    pubDateStr = item.find('.//pubDate').text
    pubDate = datetime.strptime(pubDateStr, '%a, %d %b %Y %H:%M:%S %z')
    items.append(Item(title, description, pubDate))

for item in items:
    title = fontstyle.apply(f' {item.title} ', 'BOLD/BLACK/Yellow_BG')
    pub_date = fontstyle.apply(f'({item.pubDate.strftime("%b %d, %Y")})', 'ITALIC/PURPLE')

    print(f'{title} {pub_date}\n\t{item.description[:70]}\n\t{item.description[71:140]}...')