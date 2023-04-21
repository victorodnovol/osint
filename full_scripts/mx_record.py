# mx_record.py

import dns.resolver

from .user_request import UserRequest


def run(user_request=None):
    if user_request:
        address = user_request.without_https
    else:
        address = input('Enter host: ')
        if address.endswith('/'):  # corrected
            address = address[:-1]
    my_resolver = dns.resolver.Resolver(configure=False)
    my_resolver.nameservers = ['8.8.8.8', '1.1.1.1']
    try:
        answers = my_resolver.query(address, 'MX')
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN,
            dns.resolver.NoNameservers) as e:
        print('Failed to get MX Record. Error:', e.msg)
        return
    for rdata in answers:
        UserRequest.append(f'MX Record: {rdata.exchange}')
