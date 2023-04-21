import datetime
import json
import sys
import pytz
from skyfield.api import load, N, W, wgs84
from skyfield import api, almanac
from skyfield.magnitudelib import planetary_magnitude
from itertools import zip_longest
from pathlib import Path

objects = dict()

# load data
planets = load('de421.bsp')
# This is the short file from 2008, but the data is good enough for our
# purposes

# setup time data
ts = api.load.timescale()
tz = pytz.timezone('America/Chicago')
d = datetime.datetime.now(tz=tz)  # get current time
d = d.replace(minute=0, second=0, microsecond=0)  # get hour
start_time = ts.from_datetime(
    d-datetime.timedelta(seconds=3600))  # start an hour early
end_time = ts.from_datetime(d+datetime.timedelta(days=2))  # end two day s late
times = ts.linspace(start_time, end_time)  # get list of times
unixtimes = (times.tt - 2440587.5) * 86400
timeformat = '%Y-%m-%dT%H:%M:%S%z'

# setup location
earth = planets['earth']
lapo = wgs84.latlon(37.62219*N, 97.62696*W, 421)  # good enough

# objects to view
sun = planets['sun']
mercury = planets['mercury']
venus = planets['venus']
moon = planets['moon']
mars = planets['mars']
jupiter = planets['jupiter barycenter']
saturn = planets['saturn barycenter']
uranus = planets['uranus barycenter']
neptune = planets['neptune barycenter']
pluto = planets['pluto barycenter']

objects = {}

for obj in [sun, mercury, venus, moon, mars, jupiter, saturn, uranus, neptune, pluto]:
    name = obj.target_name.split()[1].title()  # type:ignore
    objects[name] = {}
    astrometric = (earth+lapo).at(times).observe(obj)
    alt, az, earth_dist = astrometric.apparent().altaz()
    if name != 'Sun':
        sun_dist = (sun.at(times) - obj.at(times)).distance()  # type:ignore
    else:
        sun_dist = []
    try:
        mag = planetary_magnitude(astrometric).mean()
    except ValueError:
        mag = None
    phase = []
    if name == 'Moon':
        phase = (almanac.moon_phase(planets, times).degrees %
                 180) / 180  # type:ignore
    f = almanac.risings_and_settings(planets, obj, lapo)
    t, y = almanac.find_discrete(start_time, end_time, f)
    rise_set = []
    rise_set_astrometric = (earth+lapo).at(t).observe(obj)
    rise_set_alt, rise_set_dir, rise_set_dist = rise_set_astrometric.apparent().altaz()
    for ti, yi, direction in zip(t, y, rise_set_dir.degrees):
        rise_set.append(ti.astimezone(tz).strftime(timeformat) +
                        (' Rise' if yi else ' Set')+f' @ {direction}')
    meridian = []
    f = almanac.meridian_transits(planets, obj, lapo)
    t, y = almanac.find_discrete(start_time, end_time, f)
    meridian = []
    meridian_astrometric = (earth+lapo).at(t).observe(obj)
    meridian_alt, meridian_dir, meridian_dist = meridian_astrometric.apparent().altaz()
    for ti, yi, altitude in zip(t, y, meridian_alt.degrees):
        meridian.append(ti.astimezone(tz).strftime(
            timeformat) + f' @ {altitude}')
    objects[name]['earth_distance'] = {}
    objects[name]['azimuth'] = {}
    objects[name]['sun_distance'] = {}
    objects[name]['phase'] = {}
    for timestamp, sun_distance, earth_distance, phase_percent, direction in \
            zip_longest(unixtimes, sun_dist.au if sun_dist else [], earth_dist.au,  # type:ignore
                        phase, az.degrees):
        objects[name]['earth_distance'][timestamp] = earth_distance
        objects[name]['azimuth'][timestamp] = direction
        if sun_distance:
            objects[name]['sun_distance'][timestamp] = sun_distance
        if phase_percent:
            objects[name]['phase'][timestamp] = phase_percent
    objects[name]['rise_set'] = rise_set
    objects[name]['meridian'] = meridian
    objects[name]['magnitude'] = mag


outfile = Path(__file__).parent.joinpath('../solar-system/data.json')
if len(sys.argv) > 1:
    outfile = Path(sys.argv[1])

path = outfile.resolve()
json.dump(objects, open(path, 'w'), indent=2)
