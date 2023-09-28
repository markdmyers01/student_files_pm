"""

    09_namedtuples.py
    Creating the classic namedtuple.

"""
from collections import namedtuple
from dataclasses import dataclass

# c = namedtuple('Contact', 'first last age email')

@dataclass
class Contact:
    first: str
    last: str
    age: int
    email: str

c = Contact

records = [
    c('John',  'Smith',   43, 'jsbrony@yahoo.com'),
    c('Ellen', 'James',   32, 'jamestel@google.com'),
    c('Sally', 'Edwards', 36, 'steclone@yahoo.com'),
    c('Keith', 'Cramer',  29, 'kcramer@sintech.com')
]
records.sort(key=lambda one_rec: one_rec.age, reverse=True)

print(records)
records[0].age = 'Unknown'

for record in records:
    print(type(record))
    print(record.last, record.age)
