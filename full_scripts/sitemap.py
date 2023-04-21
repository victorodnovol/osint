# sitemap.py

import requests
from bs4 import BeautifulSoup

from .user_request import UserRequest


def run(user_request=None):
    if user_request:
        url = user_request.with_https
    else:
        url = input('Enter host [https://site.com]: ')
    head = {
        'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0'
    }
    if not url.endswith('/'):
        url += '/'
    try:
        page = requests.get(url + 'sitemap.xml', headers=head)
    except requests.exceptions.MissingSchema as e:
        print('Failed to get sitemap.xml. Please enter correct address')
        return
    except requests.exceptions.ConnectionError as e:
        print('Failed to connect to this host')
        return
    except requests.exceptions.RequestException as e:
        print('There was ambigous exception while handling your request')
        return
    if page.status_code == 200:
        res = BeautifulSoup(page.text, 'lxml')
        for i in res.find_all('loc'):
            UserRequest.append(i.text)
    else:
        print('File "sitemap.xml" not found!')
