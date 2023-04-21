# who_is.py
import whois

from .user_request import UserRequest


def run(user_request=None):
    if user_request:
        add = user_request.without_https
    else:
        add = input('Enter domain: ')
    try:
        domain = whois.query(add)
    except (UnknownTld, WhoisPrivateRegistry) as e:
        print('Error: ', e)
        return
    if not domain:
        print('Error: such domain not found')
        return
    res = domain.__dict__
    [UserRequest.append(f'{i}: {res[i]}') for i in res]
