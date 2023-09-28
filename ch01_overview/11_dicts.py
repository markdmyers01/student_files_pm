"""

    11_dicts.py
    Working with dictionaries.

"""
print('\nCreating and accessing dicts:')
my_dict = {}
my_dict = dict()
my_dict = {'pet1': 'dog', 'pet2': 'fish' }
my_dict = dict(pet1='dog', pet2='fish')

my_dict['pet3'] = 'cat'
my_dict['pet2'] = 'goat'
print(my_dict)


print('\nIterating dicts:')
d1 = {'Smith': 43, 'James': 32, 'Edwards': 36, 'Cramer': 29}
for item in d1:                     # iterating a dictionary returns the keys
    print(item, end=' ')


print('\n\nIterating dict values:')
for val in d1.values():             # iterating the values
    print(val, end=' ')

list1 = []
print('\nIterating keys and values:')
for item in d1.items():         # iterating both keys and values
    list1.append(item)
    # print(f'Key: {key}, Value: {val}')

print(list1)

print('\nAccessing dicts:')
print(d1.get('Green'))              # returns None
print(d1.get('Key_list', []))       # returns N/A
# print(d1['Green'])                 # generates a KeyError


print('\nSorting with dicts:')
list1 = sorted(d1)
list2 = sorted(d1.values())
print(list1, list2)

list3 = sorted(d1.items(), key=lambda item: item[1])
print(list3)

back_to_dict = dict(list3)
print(back_to_dict)