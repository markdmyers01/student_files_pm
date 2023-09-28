"""

    07_requests.py
    Makes an API request.

"""
import requests

r = requests.get("https://httpbin.org/json")
print(r.url)
print(r.status_code)
print(r.headers)
print(r.request.headers)
print(r.text)
print(r.json())


# r = requests.post("http://someURL", data = {'key': 'value'})
# r = requests.put("http://someURL", data = {'key': 'value'})
# r = requests.delete("http://someURL")
# r = requests.head("http://someURL")
# r = requests.options("http://someURL")
