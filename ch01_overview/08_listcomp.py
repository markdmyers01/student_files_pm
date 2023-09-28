"""

    08_listcomp.py
    Creation of lists using list comprehensions.

"""
import glob
import os

# print('\nDeleting slices from lists: ')
# a = [1, 2, 3, 4, 5]                 # from note on slide 57
# print(f'Before delete: {a}')
# del a[1:3]		                    # a is now [1, 4, 5]
# print(f'After delete: {a}')
#
print('\nBasic list comprehension: ')
list1 = [1, 2, 3, 4, 5]
print(list1)
list2 = [x*2 for x in list1]
print(list2)                        # [2, 4, 6, 8, 10]

print('\nList comprehension with conditional: ')
list1 = [1, 2, 3, 4, 5]
print(list1)

list2 = [x*2 for x in list1 if x % 2 == 0]
print(list2)                        # [4, 8]
print()


# -----------------------------------------------------------
# Revisiting using a list comprehension:
# print('\nRefactoring Task 1-4 to use a list comprehension:')

dir_contents = []
path = '.'
match = '*'
for pathitem in glob.glob('/'.join([path, match])):
    dir_contents.append(pathitem)

files = [(os.path.basename(item), os.path.getsize(item)) for item in dir_contents if os.path.isfile(item)]
files.sort(key=lambda fileinfo: fileinfo[1], reverse=True)

x = 0
for name, size in files:
    x += size
    print(f'{name:<20}{size}')

print(x)

print(files[:5])


total_bytes = sum([item[1] for item in files])
print(total_bytes)


print('\nExample using the positional expand operator (*):')


def avg_temperatures(fri_temp, sat_temp, sun_temp, *args, **kwargs):
    print(args, kwargs)
    return (fri_temp + sat_temp + sun_temp) / 3


temps = [88, 92, 94, 80, 82, 96]
print(avg_temperatures(*temps, region='us'))
