"""

       task1_2.py   -   Working with strings and control structures

"""
prefixes = ['http://', 'https://']
suffixes = [':', '/', '?']

url1 = 'https://docs.python.org/3/'
url2 = 'https://www.google.com?gws_rd=ssl#q=python'
url3 = 'http://localhost:8005/contact/501'

# Solving for url1
domain = url1
for prefix in prefixes:
    if url1.startswith(prefix):
        domain = url1[len(prefix):]

for suffix in suffixes:
    pos = domain.find(suffix)
    if pos != -1:
        domain = domain[:pos]

print(domain)

# -----------------------------------------------------------
# To make it work for all URLs iteratively (advanced version)
urls = [url1, url2, url3]

for url in urls:
    domain = url

    for prefix in prefixes:
        if url.startswith(prefix):
            domain = url[len(prefix):]

    for suffix in suffixes:
        pos = domain.find(suffix)
        if pos != -1:
            domain = domain[:pos]

    print(domain)
