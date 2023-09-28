"""

       task1_2_starter.py

For this task, you are to manually extract the domain name out of the URLs
mentioned on our slide.  The URLs are:

https://docs.python.org/3/
https://www.google.com?gws_rd=ssl#q=python
http://localhost:8005/contact/501


 Additional Hints:
   1. Start with one of the urls below by uncommenting it.

   2. Check if the URL begins with any of the prefixes by using .startswith()
      If it does, capture the remaining part of the URL using slicing
        Example:
                 url = 'https://docs.python.org/3/'
                 if url.startswith('http://')
                     remaining = url[len('http://'):]

      Since there is more than one prefix, we'll need to do it iteratively:

                 url = 'https://docs.python.org/3/'
                 for item in prefixes:
                     if url.startswith(item)
                         remaining = url[len(item):]


  3. Now, we'll work on the other end of the URL (the suffixes).  Be sure to use the 'remaining'
     variable from the previous step for this next step.

     Use .find() to find the position of a suffix.
     Remember, find() returns a -1 for items not found in the string.
     For example:
                 position = remaining.find(':')
                 if position != -1:
                     domain = remaining[:position]

     This code above works, but we want to do it for all of the suffixes iteratively:
                 for item in suffixes:
                     position = remaining.find(item)
                     if position != -1:
                         domain = remaining[:position]

 4. Don't forget to print out your results for each URL

 5. Advanced: Can you now make the above solution work for all URLs iteratively?
"""

prefixes = ['http://', 'https://']
suffixes = [':', '/', '?']

url1 = 'docs.python.org/3/'
url2 = 'https://www.google.com?gws_rd=ssl#q=python'
url3 = 'http://localhost:8005/contact/501'

domain = url1
for prefix in prefixes:
    if url1.startswith(prefix):
        domain = url1[len(prefix):]
        # print(domain)

for suffix in suffixes:
    pos = domain.find(suffix)
    if pos != -1:
        domain = domain[:pos]

print(domain)

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
