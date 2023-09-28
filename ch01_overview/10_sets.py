"""

    10_sets.py
    Use of the set type.

"""
s1 = set([1, 2, 3, 2])
print(len(s1))			    # outputs 3

s2 = {4, 5, 6}
print(s1.isdisjoint(s2))    # outputs True, no elements in common

s3 = frozenset([2, 4, 7])
print(s2.difference(s3))

records = set()
records.add(('John',  'Smith',   43, 'jsbrony@yahoo.com'))
records.add(('Ellen', 'James',   32, 'jamestel@google.com'))
records.add(('Sally', 'Edwards', 36, 'steclone@yahoo.com'))
records.add(('Ellen', 'James',   32, 'jamestel@google.com'))        # this one is not added since it is a duplicate
print(len(records))

# print(records[0])

for record in records:
    print(record)
