"""

       task1_3_starter.py   -   A simple grep utility


    Use the following command-line syntax run running this script:

        python task1_3_starter.py wordexpression directory

        Example:  python task1_3_starter.py print .

        (Note: within Pycharm, select Run > Edit Configurations and add wordexpression and directory
               into the parameters section)


    Detailed Tips/Suggestions:
    1. The provided starter code below retrieves the two command-line parameters (wordexpression and directory) for us.
       Look this code over.

       You should use os.listdir() to get a list of files from the specified directory.
       Iterate over the list of filenames and verify if they are all files.
       Hint: you can use os.path.isfile() to check if items are files.
       Note: another helpful tool is os.path.join(directory_name, filename).

       Use the append() method to add files into the provided file_list variable.

            items = os.listdir(directory)

            for entry in items:
                filename = os.path.join(directory, entry)
                if os.path.isfile(filename):
                    file_list.append(filename)


    2. Opening/reading/writing/closing files will be discussed further later,
       so for now, you have been shown how to read a line from a file:
        Example:

            for line in open(filename, encoding='utf-8'):
                # process line from file


        Overall your steps should be something like this:
            - Iterate over the file_list.
            - Open each file (from the list) one at a time
            - Read each line from the file in
        Example:

            for filename in file_list:
                line_count = 0
                for line in open(filename, encoding='utf-8'):

    3. Check for a match:
        Check for the presence of the wordexpression
                    Hint: Use .find() for this
                - Output a result if there is a match

                    line_count += 1
                    if line.find(word_expression) != -1:


    4. If there is a match, output line number:

    print(f'{filename}, {line_count}, {wordexpression}')


    Note: This exercise works only with text files.  Non-text files (binary
          files) will raise a UnicodeDecodeError (which can be handled, but this
          hasn't been discussed yet).
"""

import sys
import os
os.system('cls')
args = sys.argv                                                 # get command-line args
print(args)

if len(args) != 3:
    print('Insufficient arguments provided. Syntax:')
    print('python task1_3_starter.py wordexpression directory')
    sys.exit(42)

wordexpression = args[1]
directory = args[2]

file_list = []

# put your solution here
dir_contents = os.listdir(directory)
print(dir_contents)

for entry in dir_contents:
    filename = os.path.join(directory, entry)
    if os.path.isfile(filename):
        file_list.append(filename)
print(file_list)

for filename in file_list:
    line_count = 0
    for line in open(filename, encoding='utf-8'):
        line_count += 1
        if line.find(wordexpression.casefold()) != -1:
            print(f'File: {os.path.basename(filename)}, Line: {line_count}, ({wordexpression})')

# os.system("set /p DUMMY=Hit Enter to Continue")
input('Press a key to coninue')
