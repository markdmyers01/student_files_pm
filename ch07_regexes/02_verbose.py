"""

    02_verbose.py
    The verbose flag for defining regexes.

"""
import re

pattern = r'''
(\(?\d{3}\)?)?    # optional area code, parentheses optional
[-\s.]?           # opt. separator: dash, space, or period
\d{3}             # 3-digit prefix
[-\s.]            # separator: dash, space, or period
\d{4}             # final 4-digits
'''

phones = [
    '123-456-7890',
    '800 555 4400',
    '(123) 456-7890',
    '123.456.7890',
    '123-4567',
    'reallywrong',
    '1234-456-7890'
]


valid = [ph for ph in phones if re.match(pattern, ph, re.VERBOSE)]
print(valid)
print(f'Valid phones: {valid}')
print('Valid phones: {0}'.format(valid))


newStr = re.sub('seven', 'eight', 'Four score and seven years ago and in another seven years', count=1)
print(newStr)

print(re.split(r'\d+', 'hello123world'))

pattern_obj = re.compile(pattern, re.VERBOSE)
valid = [ph for ph in phones if pattern_obj.match(ph)]
print('Valid phones: {0}'.format(valid))