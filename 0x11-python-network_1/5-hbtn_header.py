#!/usr/bin/python
"""
takes in a URL, sends a request to the URL and displays the value of
the variable X-Request-Id in the response header
"""

import sys
import requests

if __name__ == '__main__':
    with requests.get(sys.argv[1]) as resp:
        print(resp.headers.get('X-Request-Id'))
