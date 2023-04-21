# checks.py
import re


def host_check(hostname):
    domain = re.match(r'\w+\.\D{2,3}', hostname)
    if domain:
        return True
