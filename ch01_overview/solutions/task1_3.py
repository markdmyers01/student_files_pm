"""

       task1_3.py   -   A simple grep utility


    The following syntax should work:
        python task1_3_starter.py wordexpression directory
        
    Note: Since we are not handling exceptions at this point, you should only 
          provide a directory name containing text files.  Non-text files (binary
          files) will raise UnicodeDecodeErrors.
"""

import sys
import os

args = sys.argv                                                 # get command-line args
if len(args) != 3:
    print('Improper arguments provided. Syntax:')
    print('python task1_3.py wordexpression directory')
    sys.exit(42)

wordexpression = args[1]
directory = args[2]
file_list = []

dir_contents = os.listdir(directory)

for entry in dir_contents:                                  # check each item if it is a file or not
    filename = os.path.join(directory, entry)
    if os.path.isfile(filename):
        file_list.append(filename)                          # add only files to the file_list

for filename in file_list:
    line_count = 0                                              # better to use enumerate() but this hasn't been discussed yet
    for line in open(filename, encoding='utf-8'):
        line_count += 1
        if line.find(wordexpression) != -1:
            print(f'File: {os.path.basename(filename)}, Line: {line_count}, ({wordexpression})')
