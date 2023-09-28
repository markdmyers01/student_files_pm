"""
    task6_1_advanced.py (Solution)  -   Using JSON, Requests, and HTML Parsing (Soup)

    This task asks you to retrieve the JSON data at the following URL:

                https://eonet.gsfc.nasa.gov/api/v3/events

    This URL provides information of events tracked by NASA.

    You should view this data in a browser to get a feel for what it contains.  Keep that browser tab open
    and then perform the following tasks:

    1) Retrieve the JSON data at the URL mentioned above.  Extract all the "events".
    2) Determine how many total events are currently being tracked by NASA (at this API).
    3) Obtain a list all the different possible categories (titles) that are tracked.
    4) Display the titles of all the fires ('Wildfires' category type)
    5) Retrieve the Inciweb HTML home page of the first wildfire being tracked (if it exists).
       This should be found under the sources[0] property of the event object.
    6) Retrieve the HTML page from the URL in step 5.  Return the fire's description (Incident Overview section).
       Do this by invoking soup's select() method, providing the given selector.

    Note: if no internet access is available, uncomment the import mocklab statement below, and you may proceed
          with the task.

"""
import sys

from bs4 import BeautifulSoup
import requests

# import mocklab                    # uncomment this line if no internet access is available


# Step 1.
class Event:
    def __init__(self, title='', categories=None, sources=None):
        self.title = title
        self.categories = [] if not categories else categories
        self.sources = [] if not sources else sources


class EONETData:
    def __init__(self, url='https://eonet.gsfc.nasa.gov/api/v3/events'):
        self.url = url
        self.events = []
        self.sync()

    def sync(self):
        # Step 2.
        resp_dict = requests.get(self.url).json()
        for event in resp_dict.get('events'):
            title = event.get('title')
            categories = event.get('categories')
            sources = event.get('sources')
            self.events.append(Event(title, categories, sources))

    # Step 3.
    @property
    def categories(self):
        categories = set()
        for event in self.events:
            for category in event.categories:
                categories.add(category.get('title'))
        return categories

    # Step 4.
    @property
    def fires(self):
        fires = []
        for event in self.events:
            for category in event.categories:
                if category.get('title') == 'Wildfires':
                    fires.append(event)
        return fires


# Step 5.
try:
    eonet = EONETData()
except requests.RequestException as err:
    print(f'{type(err).__name__}: {err}', file=sys.stderr)
    sys.exit(42)

# Step 6.
print(f'NASA tracking {len(eonet.events)} total events.')


# Step 7.
print(f'\nSeveral categories found across all events: {list(eonet.categories)}')

# Step 8.
print('\nDisplaying fires tracked:')
fires = eonet.fires
print([fire.title for fire in fires])

# Step 9.
sources = fires[0].sources
if not sources:
    print(f'No Inciweb URL found for {fires[0].title}')
    sys.exit(42)

url = sources[0].get('url')

# Step 10.
print(f'\nRetrieving page for fire at: {url}')
soup = BeautifulSoup(requests.get(url).text, 'html.parser')

print(f'\nDescription for {fires[0].title}:')
selector = '.incident-main-content p'
print(soup.select(selector)[0].text)
