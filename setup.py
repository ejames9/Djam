
from disutils.core import setup

setup(
    name = "DjamBase",
    version = "1.0.0",
    author = "Eric James Foster",
    author_email = "maniphestival@gmail.com",
    url = ""
    description = "A Thin JamBase API Client library for Django/Python Applications.",
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description = """\
===========================
JamBase API Client Library
===========================

Getting Started
----------------
Get a valid Developer API key at http://developer.jambase.com. ::

    import DjamBase

    db = DjamBase("your_api_key")

Usage
------
``db.artist_search(params)``
    -params is a dictionary, with ``{"id": *integer*, "name": *string*}`` as key, value options. These will serve
    as the search parameters.
``db.venue_search(params)``
    -params is a dictionary, with ``{"id": *integer*, "zipCode": *integer*, "radius": *integer*}`` as key, value options.
``db.event_list(params)``
    -params is a dictionary, with`` {"id": *integer*,
                                   "artist": *string*,
                                   "artistId": *integer*,
                                   "band": *string*,
                                   "bandId": *integer*,
                                   "venueId": *integer*,
                                   "zipCode": *integer*,
                                   "radius": *integer*,
                                   "startDate": *YYYY-MM-DD*,
                                   "endDate": *YYYY-MM-DD*} ``as possible key, value options.

Use any combination of the available parameters, per function, that you like, depending on the
desired results. All keys are written in "camelCase".

Use as below: ::

    r = db.event_list( {"name": "the foobar fighters", "radius": 200})


The variable "r" will contain a json response object. I will incorporate xml soon.

"""
)
