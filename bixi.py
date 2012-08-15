#!/usr/bin/env python

import argparse

import conf
import utils
import scraper


modes = ['search', 'route', 'go']

parser = argparse.ArgumentParser(description='Bixi stuff')

parser.add_argument('mode',
                    help="possible modes: %s" % ', '.join(modes))

parser.add_argument('arguments',
                    help="see the readme for the arguments for each mode",
                    nargs='+')

args = parser.parse_args()



if args.mode in modes:
    url = 'https://%s.bixi.com/maps/statajax' % conf.city
    stations = scraper.get_stations(url)

    if args.mode == 'search':
        query = args.arguments[0]
        for station_id, station in stations.iteritems():
            if query in station['name'].lower():
                print "%s: %s" % (station_id, station['name'])

    if args.mode == 'route':
        route = args.arguments[0]

        if route in conf.routes:
            start_location, end_location = conf.routes[route]

            utils.print_route_info(stations, start_location, end_location)
        else:
            parser.error("The route \"%s\" does not exist in your conf file." % route)

    if args.mode == 'go':
        if len(args.arguments) == 2:
            start_location, end_location = args.arguments

            if start_location in conf.locations and end_location in conf.locations:
                utils.print_route_info(stations, start_location, end_location)
            else:
                parser.error("At least one of your locations is not in your conf file.")
        else:
            parser.error("You must enter exactly two stations (a start and an end station).")
else:
    parser.error("See the readme for usage instructions.")
