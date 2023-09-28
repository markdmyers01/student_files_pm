"""

      task5_2_starter.py    -   Using pathlib.Path()

      Repeat Task 5-1, this time using the Path object from the pathlib module.

      The Path() object can be used to replace most of the file and directory-related
      operations from the os module.

      Work from this file, task5_2_starter.py.

"""
from pathlib import Path
import shutil

# Step 1. Replace root_directory below with a Path() object of the root_directory Path('..') instead
root_directory = '..'

# Step 2. Replace dst below with a Path() object of the 'resources/images' directory instead
dst = 'resources/images'
copied = 0

# Step 3. Iterate the root_directory using either rglob() or glob('**/*.jpg')
# Step 4. Within a try-except block that handles SameFileErrror exceptions, perform a
#         shutil.copy()

# Optionally, count the number of copies made, display the copied files count.
