# get_soa.py

from nslookup import Nslookup

from .checks import host_check
from .user_request import UserRequest


def run(user_request=None):
    if user_request:
        domain = user_request.without_https
    else:
        domain = input('Enter host: ')
        if not host_check(domain):
            print('User input is incorrect')
            return
        if domain.endswith('/'):
            domain = domain[:-1]
    dns_query = Nslookup(dns_servers=['1.1.1.1'])
    try:
        ips_record = dns_query.dns_lookup(domain)
    except AttributeError as e:
        print('Error: ', e)
        return
    for i in ips_record.response_full:
        UserRequest.append(i)
    soa_record = dns_query.soa_lookup(domain)
    for i in soa_record.response_full:
        UserRequest.append('\n'.join(i.split('. ')))
