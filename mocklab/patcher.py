import json
from pathlib import Path

patched_items = {}


def patch(module, attr, newitem):
    olditem = getattr(module, attr, object())
    if olditem is not object():
        patched_items[(module, attr)] = olditem
    setattr(module, attr, newitem)


class RequestsGet:
    """Simulates requests.get().  Used specifically for EONET and Inciweb exercise for this course."""
    def __init__(self):
        self.response = None

    def __call__(self, *args, **kwargs):
        self.requests_get(*args, **kwargs)
        return self

    def requests_get(self, url='', params=None, **kwargs):
        is_events = True if url.lower().find('events') != -1 else False
        if is_events:
            file_name = 'mock_data.txt'
        else:
            file_name = 'mock_fire.txt'

        self.response = (Path(__file__).parent / file_name).read_text()

    def json(self):
        return json.loads(self.text)

    @property
    def text(self):
        return self.response

    @property
    def content(self):
        return str(self.response).encode()
