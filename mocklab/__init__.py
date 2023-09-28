"""
    This package is used only with the JSON-based NASA EONET exercise and only when internet access
    is not available (e.g., if a proxy blocks your access to https://eonet.gsfc.nasa.gov/api/v3/events.

    To use it, uncomment the import mocklab statement in your starter file.  It
    should then mock requests.get().  Note, this is not a general purpose mock of
    requests.get() and is specifically designed for the EONET exercise only.

    mocklab should not be needed/used if access to https://eonet.gsfc.nasa.gov is available.

    Finally, in order to use mocklab, the student_files directory MUST be present on your
    sys.path (which happens automatically if running from within PyCharm).
"""
import sys

from .patcher import patch, RequestsGet

try:
    import requests
except ImportError:
    print('The requests module must first be installed before using mocklab.', file=sys.stderr)
    sys.exit(42)


patch(requests, 'get', RequestsGet())
