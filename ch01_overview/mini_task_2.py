"""

       Mini-task 2 - Accessing sequences

"""
records = [
    ('John',  'Smith',   43, 'jsbrony@yahoo.com'),
    ('Ellen', 'James',   32, 'jamestel@google.com'),
    ('Sally', 'Edwards', 36, 'steclone@yahoo.com'),
    ('Keith', 'Cramer',  29, 'kcramer@sinotech.com')
]

# Display Sally Edwards age
print(records[2][2])

for record in records:
    if record[0] == 'Sally':
        print(record[2])

# Add a new record into records
list1 = list(('Ellen', 'James',   32, 'jamestel@google.com'))
list1[0] = 'Billy'
list1[1] = 'Jones'
list1[2] = 45
records.insert(1, tuple(list1))
print(records)

# Display how many records you then have after this
print(len(records))

# Display how many fields are in the second record from the end record
print(len(records[-2]))

# Display how long Keith Cramer's email is
print(len(records[-1][3]))

l1 = [1, 2, 3,]
l2 = (4, 5, 6)
# l1 = l1 + list(l2)
l1.extend(l2)
print(type(l1))