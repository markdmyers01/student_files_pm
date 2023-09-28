"""

    04_urllib.py
    Using the urllib modules.

"""
import urllib.request
import urllib.response

url = 'https://www.yahoo.com'

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
the_page = response.read().decode()
print(the_page)


# shortened version...
from urllib.request import urlopen
the_page = urlopen('https://www.yahoo.com').read().decode()



from urllib.parse import urlparse
result = urlparse('https://docs.python.org/3/library/index.html')
print(result)