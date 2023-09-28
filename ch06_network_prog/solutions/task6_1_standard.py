"""
    task6_1_standard.py (Solution)  -   Using JSON, Requests, and HTML Parsing (Soup)

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

# import mocklab                          # uncomment this line if no internet access is available

base_url = 'https://eonet.gsfc.nasa.gov'
api_path = '/api/v3/events'


# Step 1. Combine the base_url and api_path.  Make an HTTP GET request to retrieve the
#         JSON-based data at this URL.  Retrieve all the "events" found in the
#         top-level "events" property of the JSON data.  Hint: do this using requests.get(url).json().
#         In the received dictionary, get all the events from the "events" key.
event_dict = requests.get(f'{base_url}{api_path}').json()
events = event_dict.get('events', [])

# Step 2. How many events are there?  Hint: Use the len() function on the list of events.
print(f'NASA tracking {len(events)} total events.')

# Step 3.  Obtain all the different category titles.  Hint: use a set() to store various category titles.
#          Iterate over the events, getting each event's categories.  The "categories" property is a list,
#          so iterate over the categories list also. (This means we'll need a nested for-loop).
#          A sample of the JSON data structure is shown below:
#
#  { "events": [
#        { ...
#          "categories": [
#              {
#                "id": "seaLakeIce",
#                "title": "Sea and Ice Lake"                   <--We want all of these possible values
#              }
#          ]
#        }, ...
#    ]
#  }
#
all_categories = set()
fires = []
for event in events:
    categories = event.get('categories', [])
    for category in categories:
        category_title = category.get('title')
        all_categories.add(category_title)

        if category_title == 'Wildfires':
            fires.append(event)

print(f'\nSeveral categories found across all events: {list(all_categories)}')

# Step 4. Modify the code created in step 3 above to save only the 'Wildfires' event types into a list.  Print the
#         names (titles) of all the 'Wildfires' events.  There will be quite a few.
print('\nDisplaying fires tracked:')
print([fire.get("title") for fire in fires])

# Step 5. Select the first fire from the fires in step 4.  Retrieve its associated Inciweb HTML page.
#         Extract the description (Incident Overview) from that page and display it.
first_fire = fires[0]
name = first_fire.get("title")
print(f'\nFirst fire listed: {name}')
sources = first_fire.get('sources')
if not sources:
    print(f'No Inciweb URL found for {name}')
    sys.exit(42)

url = sources[0].get('url')

# Step 6. Obtain the Incident Overview (description) for the fire source URL identified in step 5 as follows:
#         First, using the URL from the previous step, retrieve the HTML page with requests.get().text.
#         Parse the returned HTML (text) using BeautifulSoup.
#         Then using the provided selector, issue a soup.select(selector) to display the description.
print(f'Retrieving page for fire at: {url}')
soup = BeautifulSoup(requests.get(url).text, 'html.parser')

print(f'\nDescription for {name}:')
selector = '.incident-main-content p'
print(soup.select(selector)[0].text)
