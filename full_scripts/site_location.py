# site_location.py

from inspect import getsourcefile
from os.path import abspath, isfile

import pygeoip

from .user_request import UserRequest


def run(user_request=None):
    try:
        file_path = abspath(getsourcefile(lambda: 0))
    except OSError:
        print('File "GeoIPCity.dat" is missing')
        return
    if user_request:
        ip = user_request.addr
    else:
        ip = input('Enter IP: ')
    if not isfile(file_path):
        print('Error: database file is missing')
        return
    gi = pygeoip.GeoIP(file_path[:-16] + 'GeoIPCity.dat')
    try:
        city = gi.record_by_addr(ip)
    except OSError:
        print('Provided IP is incorrect')
        return None
    if city == None:
        print('Not found in the database')
        return None
    for key in city:
        if city[key] is None or city[key] == 0:
            continue
        else:
            UserRequest.append(f'{key}: {city[key]}')
