# reverse_ip.py

import requests

from .user_request import UserRequest


def run(user_request=None):
    if user_request:
        usr_req = user_request.without_https
    else:
        usr_req = input('Enter IP or domain: ')
    url = "https://api.hackertarget.com/reverseiplookup/"
    parameters = {
        'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0',
        'q': usr_req
    }
    try:
        response = requests.get(url, params=parameters)
    except requests.exceptions.MissingSchema as e:
        print('Failed to get url. Please enter correct address')
        return
    except requests.exceptions.ConnectionError as e:
        print('Failed to connect to this host')
        return
    except requests.exceptions.RequestException as e:
        print('There was ambigous exception while handling your request')
        return
    if 'error getting results' not in response.text:
        UserRequest.append(
            f'Found domains hosted on the same server as {usr_req}\n\n')
        UserRequest.append(response.text)
