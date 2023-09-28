"""

    03_http_client.py
    Uses the http.client module to make an HTTP request.  Easier to use than the
    lower level socket module.

"""
import http.client

conn = http.client.HTTPSConnection(host='docs.python.org')

conn.request(method='GET', url='/3/', body='',
             headers={'User-Agent': 'Not Mozilla'})
response = conn.getresponse()

print(f'Status: {response.status}')
print('Response: ')
print(f'{response.read().decode("utf-8")}')
