"""

    04_iterating.py
    Ways to iterate lists.

"""
week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
for day in week:
    if day != 'Sun' and day != 'Sat':
        print('Weekday: ' + day)
    if day == 'Sun':
        print('tomorrow is Mon')

records = [
    ('John',  'Smith',   43, 'jsbrony@yahoo.com'),
    ('Ellen', 'James',   32, 'jamestel@google.com'),
    ('Sally', 'Edwards', 36, 'steclone@yahoo.com'),
    ('Keith', 'Cramer',  29, 'kcramer@sintech.com')
]

for record in records:
    # print(f'{record[0]} {record[1]}, {record[2]} {record[3]}')
    print(record)

for record in records:
    print('{0} {1}, {2} {3}'.format(*record))

for first, last, age, email in records:
    print(f'{first} {last}, {age} {email}')

for first, *other, email in records:
    print(f'{first} {email}')
    if first == 'Sally':
        break

for first, last, age, email in records:
    print('{first} {last}, {age} {email}'.format(first=first, last=last, age=age, email=email))
