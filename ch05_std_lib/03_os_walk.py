"""

    03_os_walk.py
    Traversing and searching a directory subtree.

"""
import os

for (dirname, subdirs, files) in os.walk('..'):
   for filename in files:
       if filename.endswith('.txt'):
           filepath = os.path.join(dirname, filename)
           print(f'{filename:<20}{os.path.getsize(filepath):>8}   {dirname:40}')
