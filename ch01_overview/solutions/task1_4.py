"""

      task1_4.py   -   File size sorter utility

      This script will prompt for a path (and/or) pattern to search.
      It displays the list of files in order of largest to smallest

"""
import glob
import os
dir_contents = []

path = '..'
match = '*'
for pathitem in glob.glob('/'.join([path, match])):
    dir_contents.append(pathitem)

print(dir_contents)

files = []

# put your solution here
for item in dir_contents:                                                 # Step 1
    if os.path.isfile(item):
        files.append((os.path.basename(item), os.path.getsize(item)))     # Step 2

files.sort(key=lambda fileinfo: fileinfo[1], reverse=True)                # Step 3
for name, size in files:                                                  # Step 4
    print(f'{name:<30}{size}')
