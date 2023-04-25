import datetime
import json
import sys
import pytz
from skyfield.api import Loader, N, W, wgs84
from skyfield import api, almanac
from skyfield.magnitudelib import planetary_magnitude
from skyfield.data import mpc
from skyfield.constants import GM_SUN_Pitjeva_2005_km3_s2 as GM_SUN, tau, pi
from skyfield.nutationlib import iau2000b_radians
from itertools import zip_longest
from pathlib import Path

objects = dict()

# load data
load = Loader('.\\', verbose=False)
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
end_time = ts.from_datetime(d+datetime.timedelta(days=2))  # end two days late
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
        objects[name]['sun_distance'] = {}
        sun_dist = (sun.at(times) - obj.at(times)).distance()  # type:ignore
    else:
        sun_dist = []
    try:
        mag = planetary_magnitude(astrometric).mean()
    except ValueError:
        mag = None
    phase = []
    if name == 'Moon':
        objects[name]['phase'] = {}
        phase = (almanac.moon_phase(planets, times).degrees %
                 180) / 180  # type: ignore
    f = almanac.risings_and_settings(planets, obj, lapo)
    t, y = almanac.find_discrete(start_time, end_time, f)
    rise_set = []
    if len(t):
        rise_set_astrometric = (earth+lapo).at(t).observe(obj)
        rise_set_alt, rise_set_dir, rise_set_dist = rise_set_astrometric.apparent().altaz()
        for ti, yi, direction in zip(t, y, rise_set_dir.degrees):
            rise_set.append(ti.astimezone(tz).strftime(timeformat) +
                            (' Rise' if yi else ' Set')+f' @ {direction}')
    f = almanac.meridian_transits(planets, obj, lapo)
    t, y = almanac.find_discrete(start_time, end_time, f)
    meridian = []
    if len(t):
        meridian_astrometric = (earth+lapo).at(t).observe(obj)
        meridian_alt, meridian_dir, meridian_dist = meridian_astrometric.apparent().altaz()
        for ti, yi, altitude in zip(t, y, meridian_alt.degrees):
            meridian.append(ti.astimezone(tz).strftime(
                timeformat) + f' @ {altitude}')
    objects[name]['earth_distance'] = {}
    objects[name]['azimuth'] = {}
    for timestamp, sun_distance, earth_distance, phase_percent, direction, height in \
        zip_longest(unixtimes, sun_dist.au if sun_dist else [], earth_dist.au,  # type: ignore
                    phase, az.degrees, alt.degrees):
        objects[name]['earth_distance'][timestamp] = earth_distance
        objects[name]['azimuth'][timestamp] = direction
        if sun_distance:
            objects[name]['sun_distance'][timestamp] = sun_distance
        if phase_percent:
            objects[name]['phase'][timestamp] = phase_percent
    objects[name]['rise_set'] = rise_set
    objects[name]['meridian'] = meridian
    if mag:
        objects[name]['magnitude'] = mag


def risings_and_settings_kepler(target, topos, horizon_degrees=-34.0/60.0, radius_degrees=0):
    topos_at = (earth+topos).at
    h = horizon_degrees - radius_degrees

    def is_body_up_at(t):
        t._nutation_angles_radians = iau2000b_radians(t)
        return topos_at(t).observe(target).apparent().altaz()[0].degrees > h
    is_body_up_at.step_days = 0.25
    return is_body_up_at


def meridian_transits_kepler(target, topos):
    topos_at = (earth+topos).at

    def west_of_meridian_at(t):
        t._nutation_angles_radians = iau2000b_radians(t)
        ra1, _, _ = topos.at(t).radec(epoch='date')
        ra2, _, _ = topos_at(t).observe(target).apparent().radec(epoch='date')
        return (ra1.radians - ra2.radians) % tau < pi
    west_of_meridian_at.step_days = 0.4
    return west_of_meridian_at


asteroids = ['(1) Ceres', '(2) Pallas', '(3) Juno', '(4) Vesta']
with load.open('.\\docs\\init\\MPCORB.excerpt.DAT') as f:
    minor_planets = mpc.load_mpcorb_dataframe(f)
bad_orbits = minor_planets.semimajor_axis_au.isnull()
minor_planets = minor_planets[~bad_orbits]
minor_planets = minor_planets.set_index('designation', drop=False)
for name in asteroids:
    objects[name] = {}
    row = minor_planets.loc[name]
    obj = sun + mpc.mpcorb_orbit(row, ts, GM_SUN)
    astrometric = (earth+lapo).at(times).observe(obj)
    alt, az, earth_dist = astrometric.apparent().altaz()
    f = risings_and_settings_kepler(obj, lapo)
    t, y = almanac.find_discrete(start_time, end_time, f)
    rise_set = []
    if len(t):
        rise_set_astrometric = (earth+lapo).at(t).observe(obj)
        rise_set_alt, rise_set_dir, rise_set_dist = rise_set_astrometric.apparent().altaz()
        for ti, yi, direction in zip(t, y, rise_set_dir.degrees):
            rise_set.append(ti.astimezone(tz).strftime(timeformat) +
                            (' Rise' if yi else ' Set')+f' @ {direction}')
    f = meridian_transits_kepler(obj, lapo)
    t, y = almanac.find_discrete(start_time, end_time, f)
    meridian = []
    if len(t):
        meridian_astrometric = (earth+lapo).at(t).observe(obj)
        meridian_alt, meridian_dir, meridian_dist = meridian_astrometric.apparent().altaz()
        for ti, yi, altitude in zip(t, y, meridian_alt.degrees):
            meridian.append(ti.astimezone(tz).strftime(
                timeformat) + f' @ {altitude}')
    objects[name]['earth_distance'] = {}
    objects[name]['azimuth'] = {}
    objects[name]['sun_distance'] = {}
    for timestamp, sun_distance, earth_distance, direction, height in \
        zip_longest(unixtimes, sun_dist.au if sun_dist else [],  # type: ignore
                    earth_dist.au, az.degrees, alt.degrees):
        objects[name]['earth_distance'][timestamp] = earth_distance
        objects[name]['azimuth'][timestamp] = direction
        objects[name]['sun_distance'][timestamp] = sun_distance
    objects[name]['rise_set'] = rise_set
    objects[name]['meridian'] = meridian


outfile = Path(__file__).parent.joinpath('../solar-system/data.json')
if len(sys.argv) > 1:
    outfile = Path(sys.argv[1])

path = outfile.resolve()
json.dump(objects, open(path, 'w'), indent=2)
