"""

    12_requests_login.py
    The following example uses the requests Python module to
    login to a website, then load a page that is normally only
    accessible AFTER logging in.

    It does this by using the following url to login:

    https://foodclub.org/sample/login

    with the credentials of user_id=sample, password=password

    To perform your own login on your own specific web pages using
    requests, you should:

    1. identify the URL used to perform a login.  This will generally
       be a POST request, by the way.
    2. identify the form parameters used to submit the request.  One
       way to do this is to go to a browser like chrome or firefox and
       perform a login the normal way.  Use a tool like Firebug or
       Chrome Developer Tools to inspect the login and see what data
       was submitted.  Then you can use this data to perform the login
       via requests.

    In the example below, a POST login is made using requests to
    the url: https://foodclub.org/sample/login

"""
import requests
from bs4 import BeautifulSoup

payload = {
    'user_id': 'sample',
    'password': 'sample',
    'login': 'Login',
    'client_date_string': 'Thu Sep 07 2022 14:09:47 GMT-0600 (Mountain Standard Time)',
    'tz_offet': -6
}

with requests.Session() as session:
    req = session.post('https://foodclub.org/sample/login', data=payload, headers={ 'foo': 'bar'})
    req2 = session.get('https://foodclub.org/sample/bookkeeper')

    soup = BeautifulSoup(req2.text, 'html.parser')
    all_spans = soup.find_all('span')

    for one_span in all_spans:
        print(one_span.text)
