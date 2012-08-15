import urllib
import re
import json


def get_stations(url):
    response = urllib.urlopen(url)
    content = ''.join(response.readlines())

    # Go through the Javascript, looking for `var station`s
    # Best API ever
    matches = re.findall('var station = [^;]+;', content)

    stations = {}

    for match in matches:
        station_json = match[match.index('{'):match.index('}') + 1]

        # Have to double-quote all the keys before loading it
        station_json = re.sub('(?P<prefix>[{,])(?P<key>[^:]+):', '\g<prefix>"\g<key>":', station_json)

        # Some stations have unnecessarily escaped single quotes - fix that
        station_json = station_json.replace("\\'", "'")
        station = json.loads(station_json)

        # Save it in the stations dictionary
        station_id = station['id']
        stations[station_id] = {
            'docks': station['nbEmptyDocks'],
            'bikes': station['nbBikes'],
            'name': station['name'],
        }

    return stations
