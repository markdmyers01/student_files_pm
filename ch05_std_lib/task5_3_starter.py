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


# Step 0. In your browser, type in the url above to view the RSS feed XML structure
#         (do this if you have internet access, otherwise view archived.xml).

# Step 1. Iterate over each item and extract the title, description, and pubDate fields.  Use tree.findall('.//item')
#         to iterate over each <item>
# Example:
#              for item in tree.findall('.//item'):
#                  title = item.find('.//title').text
#                  (repeat for the other two)
items = []

# Step 2. For each item, place the field value into an Item namedtuple (already created for you above)
# Step 3. Place the namedtuple into a list (already created for you above)
#  Example:
#     items.append(Item(title, description, pubDate))

# Step 4. Display your results (in a way of your choosing) afterwards