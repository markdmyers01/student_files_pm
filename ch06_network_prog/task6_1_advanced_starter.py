"""
    task6_1_advanced_starter.py   -   Using JSON, Requests, and HTML Parsing (Soup)

    This task asks you to retrieve the JSON data at the following URL:

                https://eonet.gsfc.nasa.gov/api/v3/events

    This URL provides information of events tracked by NASA.

    You should view this data in a browser to get a feel for what it contains.  Keep that browser tab open
    and then perform the following tasks:

    1) Complete the Event class
    2) Create the categories() property
    3) Create the fires() property
    4) Retrieve the JSON data at the URL mentioned above.  Extract all the "events".
    5) Determine how many total events are currently being tracked by NASA (at this API).
    6) Obtain a list all the different possible categories (titles) that are tracked.
    7) Display the titles of all the fires ('Wildfires' category type)
    8) Retrieve the Inciweb HTML home page of the first wildfire being tracked (if it exists).
       This should be found under the sources[0] property of the event object.
    9) Retrieve the HTML page from the URL in step 5.  Return the fire's description (Incident Overview section).
       Do this by invoking soup's select() method, providing the given selector.

    Note: if no internet access is available, uncomment the import mocklab statement below, and you may proceed
          with the task.

"""
import sys

from bs4 import BeautifulSoup
import requests

# import mocklab                    # uncomment this line if no internet access is available


# Step 1. Create a class called Event.  Give it an __init__ that takes 3 parameters:
#         title='', categories=None, sources=None.
#         Within the __init__, attach the title to the self.  Before attaching categories and sources, you
#         should check if they were provided, like this:
#             self.categories = [] if not categories else categories
#         The sources parameter should be handled in a similar way as categories.


class EONETData:
    def __init__(self, url='https://eonet.gsfc.nasa.gov/api/v3/events'):
        self.url = url
        self.events = []
        self.sync()

    def sync(self):
        # Step 2. In the blank line below, retrieve the JSON data
        #         from the URL and convert it to a dict.
        #         Save the dict to a variable called resp_dict

        for event in resp_dict.get('events'):
            title = event.get('title')
            categories = event.get('categories')
            sources = event.get('sources')
            self.events.append(Event(title, categories, sources))

    @property
    def categories(self):
        categories = set()
        # Step 3. Complete this property so that it returns all the possible category types.
        #         Do this by iterating over the self.events, then iterating over the event.categories.  Add
        #         the category.get('title') into the provided set.  Return the set (or a list from the set).
        #         If it is helpful, refer to the slide showing the format of the returned JSON data.

        return categories

    @property
    def fires(self):
        fires = []
        # Step 4. Complete this property so that it returns all the fire (Wildfires) event types.
        #         Do this by iterating over the self.events, then iterating over the event.categories (in each event).
        #         Check if the category.get('title') is the value 'Wildfires'
        #         If so, add it to the fires list.  Return the list.
        return fires




try:
    # Step 5. Remove the pass statement and then instantiate an EONETData object
    # in this try-block.  This will automatically make the request to retrieve JSON data.
    pass
except requests.RequestException as err:
    print(f'{type(err).__name__}: {err}', file=sys.stderr)
    sys.exit(42)

# Step 6. How many events are being monitored by NASA?
#         Hint: Check the len() of the returned EONETData() object's events attribute.


# Step 7. Determine all the different category types.  Do this by executing the EONETData() object's categories
#         property (created in step 3).


# Step 8. Display a list of all the fires.  Do this by executing the EONETData() object's fires property
#         (created in step 4).


# Step 9. Get the URL for the HTML page that summarizes the first fire in our events.
#         Use the sources attribute of the fires[0] object.  Check if it exists (just to be safe).
#         If so, access the sources list, get the first item using sources[0].  This is a dict that
#         should have a 'url' key.  Get this key--this is your first fire URL.


# Step 10. With the URL, make a requests.get() call, then get the text from it.  Use this text and pass it into
#         BeautifulSoup to parse the HTML.  From there use the selector provided below and the soup.select() method
#         to discover the Incident Overview (description).

selector = '.incident-main-content p'
