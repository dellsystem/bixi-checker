import urllib
import re
import json


def get_stations(city):
    url = 'https://%s.bixi.com/maps/statajax' % city
    response = urllib.urlopen(url)
    content = ''.join(response.readlines())

    # Go through the Javascript, looking for `var station`s
    # Best API ever
    matches = re.findall('var station = [^;]+;', content)

    stations = {}

    for match in matches:
        # Take everything between the { and the closing } (inclusive)
        station_json = match[match.index('{'):match.index('}') + 1]

        # Have to double-quote all the keys before loading it
        # If there's extra whitespace before the key, ignore it
        station_json = re.sub('(?P<prefix>[{,])[ ]?(?P<key>[^:]+):', '\g<prefix>"\g<key>":', station_json)

        # Some stations have unnecessarily escaped single quotes - fix that
        station_json = station_json.replace("\\'", "'")
        station = json.loads(station_json)

        # Save it in the stations dictionary
        station_id = int(station['id'])
        stations[station_id] = {
            'docks': int(station['nbEmptyDocks']),
            'bikes': int(station['nbBikes']),
            'name': station['name'],
            'longitude': float(station['long']),
            'latitude': float(station['lat']),
            'installed': bool(station['installed']),
            'locked': bool(station['locked']),
            'temporary': bool(station['temporary']),
            'sponsor_name': station['sponsorName'],
            'sponsor_link': station['sponsorLink'],
            'sponsor_logo': station['sponsorLogo'],
        }

    return stations
