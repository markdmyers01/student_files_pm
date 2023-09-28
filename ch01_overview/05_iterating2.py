"""

    05_iterating2.py
    Additional ways to iterate lists.

"""
records = [
    ('John',  'Smith',   43, 'jsbrony@yahoo.com'),
    ('Ellen', 'James',   32, 'jamestel@google.com'),
    ('Sally', 'Edwards', 36, 'steclone@yahoo.com'),
    ('Keith', 'Cramer',  29, 'kcramer@sintech.com')
]

for idx, contact in enumerate(records, 10):
    print(idx, contact[1])

for contact in reversed(records):
    print(contact[1])

for idx, contact in enumerate(reversed(records), start=1):
    print(idx, contact[1])

fruit = ['Apple', 'Orange', 'Banana', 'Watermelon', 'Blueberry']
color = ['red', 'orange', 'yellow', 'green', 'blue']

list1 = []
for f, c, r in zip(fruit, color, records):
    list1.append((f, c))
    # print((f, c))
    print(f'The {f} is {c}')
print(dict(list1))