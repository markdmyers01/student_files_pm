"""

    04_writing.py
    Using a context manager to write to a file.

"""
import os.path
import sys

data = [
    'Lorem ipsum dolor sit amet, consectetur ',
    'adipiscing elit, sed do eiusmod tempor incididunt',
    'ut labore et dolore magna aliqua. Ut enim ad minim',
    'veniam, quis nostrud exercitation ullamco laboris',
    'nisi ut aliquip ex ea commodo consequat. Duis aute',
    'irure dolor in reprehenderit in voluptate velit esse',
    'cillum dolore eu fugiat nulla pariatur. Excepteur',
    'sint occaecat cupidatat non proident, sunt in culpa',
    'qui officia deserunt mollit anim id est laborum.',
]

try:
    # if os.path.exists('data.txt'):
    with open('data.txt', encoding='utf-8') as f:
        x = f.read()
        print(type(x))
        # for item in data:
        #     print(item, file=f)
except IOError as err:
    print(err, file=sys.stderr)
