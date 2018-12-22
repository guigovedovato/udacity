#!/usr/bin/env python3
import httplib2
import json


def getGeocodeLocation(inputString):
    google_api_key = ""
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?\
           address={}&\
           key={}'
           .format(locationString, google_api_key))
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude, longitude)
