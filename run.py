from flask import Flask, request, redirect
import twilio.twiml

from bixiapi import scraper, conf


app = Flask(__name__)


def get_location_info(stations, location, looking_for):
    location = str(location).lower()
    if location in conf.locations:
        for station_id in conf.locations[location]:
            try:
                station = stations[station_id]
            except KeyError:
                # Can't find it in the API, weird
                continue

            num_things = station[looking_for]

            station_name = conf.stations.get(station_id, station['name'])

            if num_things > 0:
                return "%s: %d %s" % (station_name, num_things, looking_for)

        # Nothing has been found
        return "No stations with %s near %s" % (looking_for, location)
    else:
        return "Invalid location: %s" % location


@app.route("/", methods=['GET', 'POST'])
def process_request():
    stations = scraper.get_stations(conf.city)
    body = request.values.get('Body')

    station_info = []

    locations = body.strip().split(' ')

    # If there are two, first is the start, last is the end
    if len(locations) == 2:
        start_location = locations[0]
        end_location = locations[1]

        station_info.append(get_location_info(stations, start_location,
'bikes'))
        station_info.append(get_location_info(stations, end_location, 'docks'))
    else:
        # Show bike and dock info for every station
        for location in locations:
            station_info.append(get_location_info(stations, location, 'bikes'))
            station_info.append(get_location_info(stations, location, 'docks'))

    resp = twilio.twiml.Response()
    resp.sms("\n".join(station_info))
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
