Bixi Checker
============

A simple command-line script that I created to simplify checking the status of your favourite bixi stations. It can handle multiple stations per location, routes (start and end locations only), and custom names for stations.

Requires Python 2.7+.

Simple example
--------------

To check if there's a route from home to work:

```
$: ./bixi go home work
Nearest to home: 15 bikes
Nearest to work: 27 docks
```

Setup instructions
------------------

1. Clone this repository.
2. Copy conf.py.sample to conf.py.
3. Find the IDs for the stations you're interested in. To simplify this process, there's a lookup feature included in this program, in the `search` mode. For example, to find all the bixi stations on Sherbrooke, just type `./bixi.py search sherbrooke` and you'll get a list of ID-name pairs. This feature currently doesn't handle non-ASCII characters (it will soon).
4. Add the desired station IDs and locations to conf.py. You only need to add a station ID to the `stations` dictionary if you want to give it a custom name (otherwise, it will show the official name, which is usually the intersection). Note that location names should not contain a space.
5. To find a suitable route from one location to another, simply type `./bixi.py START END` where START is the name you gave to the location you are departing from and END is the name you gave to the location you are arriving at. The script will then look at each of the stations you listed for the starting location, in order, and will print out the first one with an available bike; similarly, for the ending location, it will print out the first one with an available dock. If no stations are available, it will tell you that instead.
6. If you there is a route that you take frequently, you can add it to the route dictionary at the bottom. Simply enter the starting location and the ending location as a tuple `(START, END)`.

Modes
-----

* `search`: `./bixi.py search QUERY`
* `go`: `./bixi.py go START_LOCATION END_LOCATION`
* `route`: `./bixi.py route ROUTE_NAME`

API
---

As bixi.com doesn't seem to have an official API (just some dynamically-generated Javascript), I've created a Python module, bixiapi.py, that wraps around it. `bixiapi` exposes one method - the `get_stations()` method - which takes in the identifier for the desired city (either "montreal", "toronto", or "capitale")and returns a dictionary containing the information for all the stations in that city. Any required type conversion is taken care of (as the bixi.com website returns everything as a string).

The format looks like this:

```python
{
    # Key: station ID (as used internally, but converted to an int)
    1: {
        'docks': 10, # converted to an int
        'bikes': 10, # converted to an int
        'name': 'Street 1 / Street 2',
        'longitude': -77.7, # converted to a float
        'latitude': 44.4, # converted to a float
        'installed': true, # converted to a bool
        'locked': false, # converted to a bool
        'temporary': false, # converted to a bool
        'sponsor_name': None, # either a string or None
        'sponsor_link': None, # either a string or None
        'sponsor_logo': None, # either a string or None
    },
    # ...
}
```

Usage example

```python
import bixiapi

stations = bixiapi.get_stations('montreal')

for station_id, station_data in stations:
    print station_id
    print station_data['name']
```

License
-------

MIT license.
