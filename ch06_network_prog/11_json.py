"""

    11_json.py
    Parsing and assembling JSON via Python.
"""
from collections import namedtuple
import datetime
import json


# converts a dictionary into JSON format
obj = {'task': 'run 5 miles', 'goal': 40}
print('obj is converted to a JSON string:')
print(json.dumps(obj, indent=4))


# converts a namedtuple object to a JSON format
Contact = namedtuple('Contact', 'first last age email')
contact = Contact('John',  'Smith',   43, 'jsbrony@yahoo.com')
print('\nContact namedtuple is converted to a JSON string:')
print(json.dumps(contact._asdict(), indent=4))


# converts JSON string into Python objects (dictionaries)
print('\nJSON string converted to a dict:')
new_obj = json.loads('{"first": "John","last": "Smith","age": 43,"email": "jsbrony@yahoo.com"}')
print(new_obj)


# Class objects converted to JSON
class Player:
    def __init__(self, first, last, salary, year):
        self.first = first
        self.last = last
        self.salary = salary
        self.year = year


print('\nA Player object is converted to JSON:')
p1 = Player('John', 'Smith', 30000000, 1985)
print(json.dumps(p1, default=lambda player: player.__dict__))


# what about non-serializable fields such as birthdate???
class Player2:
    def __init__(self, first, last, salary, year, birthdate):
        self.first = first
        self.last = last
        self.salary = salary
        self.year = year
        self.birthdate = birthdate


bd = datetime.date(1970, 10, 20)
p2 = Player2('Ed', 'Green', 22000000, 198, bd)
try:
    print(json.dumps(p2, default=lambda player: player.__dict__))
except AttributeError as err:
    print('\nException: A Player object with a birthdate is unable to convert to JSON.')


# To fix the above failure....create an encoder class that defines how to handle certain types
class PlayerEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            result = obj.__dict__
        except (AttributeError, TypeError):
            if isinstance(obj, datetime.date):
                result = obj.isoformat()
            else:
                result = 'unable to determine'

        return result


print('\nThe player can now be converted when a JSONEncoder is used:')
p3 = Player2('Tom', 'Summers', 18000000, 1991, bd)
print(json.dumps(p3, cls=PlayerEncoder))
