"""

    06_list_del.py
    Illustrates using the del operator to remove a single or multiple items from a list.

"""
data = None
a = [1, 'foo', (), 3.3, str(data), data]
print(a)                                     # [1, 'foo', (), 3.3, 'None', None]

# remove 2nd item
del a[1]
print(a)                                     # [1, (), 3.3, 'None', None]

# remove first and second
# items after last removal
del a[0:2]
print(a)                                    # [3.3, 'None', None]

