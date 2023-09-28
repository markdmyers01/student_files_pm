"""

    06_match_case.py
    Illustrates the use and variations of the match-case control.
    Example requires python 3.10+ to run.

"""
import sys

from urllib.request import urlopen
from urllib.error import URLError, HTTPError

results = ''

url200 = 'https://httpbin.org'
url404 = 'https://httpbin.org/foo'
url403 = 'https://httpbin.org/status/403'


try:
    with urlopen(url200) as f:
        results = f.read().decode('utf-8')
        print(results)
except HTTPError as err:
        match err.code:
            case 404:
                print('Page not found.  Bad URL.', file=sys.stderr)
            case 403:
                print('Access denied.', file=sys.stderr)
            case _:
                print('An HTTP error occurred.', file=sys.stderr)
except URLError as err:
    print(f'Error: {err}', file=sys.stderr)


print('\n-----------\n')
print('Example of pattern matching of match-case...')

# The pattern matching feature of the match-case control...
expressions = 'one', 1, (1, ), (1, 2, 3), [1, 2, 4], (1, 2, 4, 5, 3), 2

for expr in expressions:
    match expr:
        case 1 | 2:
            print('One or two')
        case [x]:
            print('Match on any single value in sequence: ', x)
        case [1, x, 3]:
            print('Match 1 at begin, any middle, 3 at end, ', x)
        case (1, x, y):
            print('Match 1 at begin, any middle and end,', x, y)
        case 1:
            print('One again')       # only one case will work
        case [1, *x, 3]:
            print('Match 1 at begin, multiple middle, 3 end, ', x)
        case _:
            print('Default condition (match anything).')
