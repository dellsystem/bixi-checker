import conf


def print_route_info(stations, start_location, end_location):
    print get_location_info(stations, start_location, 'bikes')
    print get_location_info(stations, end_location, 'docks')


def get_location_info(stations, location, looking_for):
    for station_id in conf.locations[location]:
        station = stations[unicode(station_id)]
        # Either the number of bikes or number of docks
        num_things = int(station[looking_for])

        if num_things > 0:
            try:
                station_name = conf.stations[station_id]
            except KeyError:
                station_name = station['name']

            return "%s: %d %s" % (station_name, num_things, looking_for)

        # Nothing has been found
        return "No stations with %s found near %s! Add a new station?" % (
            looking_for,
            location,
        )
