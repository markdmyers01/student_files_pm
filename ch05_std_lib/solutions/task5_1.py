"""

      task5_1.py    -   Using os.walk()

      Create a script, using os.walk(), to find the two .jpg images
      hidden within the student_files.

      Make a copy of these files and place them into the
      student_files/resources/images folder.

      Warning!!!: If you try to copy files into the same directory,
                  you will get a SameFileError exception.  (We will walk the
                  resources/images directory and we are copying files into this
                  location also).
                  There are three ways around this:
                  1. Handle SameFileError exceptions (doing nothing in the except block)
                  2. Exclude the destination from being walked

      We'll use #2 above.
"""
import os
import shutil

root_directory = '../..'
dst = 'resources/images'
copied = 0
dstpath = os.path.abspath(os.path.join(root_directory, dst))


for curdir, subdirs, files in os.walk(root_directory):
    path = os.path.abspath(curdir)
    if path != dstpath:                             # ensure we don't walk our dstpath
        for filename in files:
            if filename.lower().endswith('.jpg'):
                print(f'Found: {filename} in {path}')
                filepath = os.path.join(path, filename)
                shutil.copy(filepath, dstpath)
                copied += 1

print(f'Copied: {copied} files to dstpath')
