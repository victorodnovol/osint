# reverse_dns.py

from dns import resolver, reversename

from .user_request import UserRequest


def run(user_request=None):
    if user_request:
        ip = user_request.addr
    else:
        ip = input('Enter IP: ')
    try:
        rev_name = reversename.from_address(ip)
        reversed_dns = str(resolver.query(rev_name, 'PTR')[0])
        UserRequest.append(reversed_dns)
    except Exception as e:
        print(e)
