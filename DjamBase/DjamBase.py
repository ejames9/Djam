"""
Jambase API Client for Django/Python Applications

Author: Eric James Foster
Version: 1.0.0

"""

import requests


class DjamBase(object):

    api_key = ""
    base_url = "http://api.jambase.com/"

    def __init__(self, key):
        self.api_key = key

    def event_list(self, params):
        url = self.base_url + "events?" + "o=json&api_key=%s"  % self.api_key.lower()
        r = requests.get(url, params=params)
        print "Status Code: " + str(r.status_code), "--- URL: " + r.url
        return r.json()


    def artist_search(self, params):
        url = self.base_url + "artists?" + "o=json&api_key=%s"  % self.api_key.lower()
        r = requests.get(url, params=params)
        print url
        print "Status Code: " + str(r.status_code), "--- URL: " + r.url
        return r.json()


    def venue_search(self, params):
        url = self.base_url + "venues?" + "o=json&api_key=%s"  % self.api_key.lower()
        r = requests.get(url, params=params)
        print "Status Code: " + str(r.status_code), "--- URL: " + r.url
        return r.json()





db = DjamBase("ENH5RHKCT65RVZKKMARYK38B")

r = db.event_list( {"band": "phish"} )
print r
