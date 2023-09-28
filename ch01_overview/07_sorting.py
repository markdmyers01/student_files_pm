"""

    07_sorting.py
    Techniques for sorting sequences.

"""
# Example 1: in-place sort
print('Basic sort: ')
items = [37, 2, 0, -14]
items.sort()
print(items)               # [-14, 0, 2, 37]


# Example 2: creating a new list by sorting
items = (37, 2, 0, -14)
new_items = sorted(items)
print(new_items)           # [-14, 0, 2, 37]


# sorting in reverse (both in-place and returning a new list)
print('\nUsing reverse=True: ')
items = [37, -14, 0, 2]
items.sort(reverse=True)
print(items)

items = [37, -14, 0, 2]
new_items = sorted(items, reverse=True)
print(items, new_items)


# not the expected sort results
print('\nUnexpected sort results: ')
nums = ['13', '1', '11', '4']
nums.sort()
print(nums)                     # ['1', '11', '13', '4']

print('\nUsing key= ')
# sort() using a key
def sort_func(val):
    return int(val)

f1 = sort_func
print(type(f1))
print(f1('10'))

nums.sort(key=sort_func)
print(nums)                     # ['1', '4', '11', '13']


# sorted() using a key
def sort_func(val):
    return int(val)
nums2 = sorted(nums, key=sort_func)
print(nums2)                    # ['1', '4', '11', '13']


# lambda examples
print('\nExamples with Lambdas:')
calc_square = lambda val: val*val
print(type(calc_square))
print(calc_square(10))


# sorting records using a key and lambda
print('\nSorting using lambdas:')
records = [
    ('John', 'Smith', 43, 'jsbrony@yahoo.com'),
    ('Ellen', 'James', 32, 'jamestel@google.com'),
    ('Sally', 'Edwards', 36, 'steclone@yahoo.com'),
    ('Keith', 'Cramer', 29, 'kcramer@sintech.com')
]

def sort_func2(record):
    return record[2]

# records.sort()
records.sort(key=lambda one_rec: one_rec[2], reverse=True)

for record in records:
    print(record)
