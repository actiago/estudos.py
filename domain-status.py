#!/usr/bin/env python
import requests
from collections import namedtuple

WebsiteStatus = namedtuple('WebsiteStatus', ['status_code', 'reason'])
names = [
    'meudominio.com'
    ]


def get_status(site):
    try:
        response = requests.head(site, timeout=5)
        status_code = response.status_code
        reason = response.reason
    except requests.exceptions.ConnectionError:
        status_code = '000'
        reason = 'ConnectionError'
    website_status = WebsiteStatus(status_code, reason)
    return website_status


for name in names:
    site = 'http://{}.com'.format(name)
    website_status = get_status(site)
    print("{0:30} {1:10} {2:10}"
          .format(site, website_status.status_code, website_status.reason))

