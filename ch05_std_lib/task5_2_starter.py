"""

      task5_2_starter.py    -   Using pathlib.Path()

      Repeat Task 5-1, this time using the Path object from the pathlib module.

      The Path() object can be used to replace most of the file and directory-related
      operations from the os module.

      Work from this file, task5_2_starter.py.

"""
from pathlib import Path
import shutil

root_directory = Path('..')
dst = root_directory / 'resources/images'
copied = 0

for pathitem in root_directory.glob('**/*.jpg'):
    try:
        shutil.copy(pathitem, dst)
        print(f'Match: {pathitem}. Copying...')
        copied += 1
    except shutil.SameFileError as err:
        pass

print(f'Copied: {copied} files to dstpath')
