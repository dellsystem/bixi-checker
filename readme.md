Bixi Checker
============

A simple command-line script that I created to simplify checking the status of your favourite bixi stations. It can handle multiple stations per location, routes (start and end locations only), and custom names for stations.

Requires Python 2.7+.

Simple example
--------------

To check if there's a route from home to work:

```
waldo@dell-laptop bixi $: ./bixi.py go home work
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

License
-------

MIT license.
