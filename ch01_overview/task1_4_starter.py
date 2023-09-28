"""

      task1_4_starter.py   -   File size sorter utility

      This script will prompt for a path (and/or) pattern to search.  It should
      display a list of files matching that path in order of largest to smallest

"""
import glob
import os
dir_contents = []

path = '.'
match = '**/*.py'
filepath = './**/*'  # '/'.join([path, match])
for pathitem in glob.glob(filepath, recursive=True):             # Lists ./*
    dir_contents.append(pathitem)

print(dir_contents)

files = []

# put your solution here
for item in dir_contents:
    if os.path.isfile(item):
        files.append((os.path.basename(item), os.path.getsize(item)))

files.sort(key=lambda fileinfo: fileinfo[1], reverse=True)

print(files)
for name, size in files:
    print(f'{name:<20}{size}')