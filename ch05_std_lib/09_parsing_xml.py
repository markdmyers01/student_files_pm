"""

    09_parsing_xml.py
    Using ElementTree to parse XML.

"""
import sys
from collections import namedtuple
from xml.etree.ElementTree import ElementTree, ParseError


Contact = namedtuple('Contact', 'first last age email')
try:
    tree = ElementTree().parse('../ch05_std_lib/results.xml')
except ParseError as err:
    print(f'Parse error: {err}', file=sys.stderr)
    sys.exit(42)

contacts = []

for contact in tree.iter('contact'):
    try:
        first = contact.find('.//first').text
        last = contact.find('.//last').text
        age = contact.get('age')
        email = contact.find('.//email').text
        contacts.append(Contact(first, last, int(age), email))
    except AttributeError as err:
        print(f'Element error: {err}', file=sys.stderr)

print(contacts)
