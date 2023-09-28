"""

    01_matching.py
    Illustrating the difference between re.match() and re.search().

"""
import re


def find(pattern, search_str):
    if re.match(pattern, search_str):
        print(f'Begins with {pattern}')
    else:
        print(f'{pattern} not found at beginning')

    if re.search(pattern, search_str):
        print(f'Contains {pattern}')
    else:
        print(f'{pattern} not found within')


# speech refers to gettysburg address, "Four score and seven years ago, ..."
speech = open('../resources/gettysburg.txt').read()
find('seven', speech)
find('four', speech)
find('Four', speech)

matchobj = re.search('seven', speech)
print(type(matchobj))
if matchobj:
    print(f'seven found at position: {matchobj.start()}')



matchobj = re.search(r'(\w+) (\w+) (\w+)', 'Four score and seven years ago')
print(matchobj.groups())                # ('Four', 'score', 'and')
print(matchobj.group(0))                # Four score and
print(matchobj.group(1))                # Four
print(matchobj.group(2))                # score
print(matchobj.group(3))                # and

str_matches = re.findall(r'\w+', 'Four score and seven years ago')
print(f'How many words: {len(str_matches)}')
print(str_matches)
