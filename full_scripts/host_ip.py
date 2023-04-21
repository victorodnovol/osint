# host_ip.py

import socket

from .user_request import UserRequest


def run(user_request=None):
    if user_request:
        host = user_request.without_https
    else:
        host = input('Enter host: ')
        if '://' in host:
            host = host.split('://')[1]
        host = host.replace('/', '')
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror as e:
        print('Error: ', e)
        return
    UserRequest.append(f'Address of {host} is {remote_ip}')
