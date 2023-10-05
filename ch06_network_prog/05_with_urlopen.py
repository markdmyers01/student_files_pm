"""

    05_with_urlopen.py
    Using the with control and URLError and HTTPError classes.

"""
import sys

from urllib.request import urlopen
from urllib.error import URLError, HTTPError

results = ''

url200 = 'https://httpbin.org'
url404 = 'https://httpbin.org/foo'
url403 = 'https://httpbin.org/status/403'


try:
    with urlopen(url403) as f_url:
        results = f_url.read().decode('utf-8')
        print(results)
except HTTPError as err:
        if err.code == 404:
            print('Page not found.  Bad URL.', file=sys.stderr)
        elif err.code == 403:
            print('Access denied.', file=sys.stderr)
        else:
            print('An HTTP error occurred.', file=sys.stderr)
except URLError as err:
    print(f'Error: {err}', file=sys.stderr)
