"""

       Mini-task 1 - f-strings and slicing (solution)

"""
ua = 'Mozilla/5.0 (Windows NT 10.0)'

left = ua.find('(')
right = ua.find(')')
if left != -1 and right != -1:
    print(f'OS: {ua[left+1:right]}')


# Fancier with regexes, but not assigned:
import re
pattern=r'(\()([^)]+)(\))'      # ( grouped, 1 or more non ) chars, ) grouped
result = re.search(pattern, ua)
if result:
    print(f'OS: {result.group}')
