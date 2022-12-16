#!/usr/bin/python3
"""
fetch https://intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopn('https://intranet.hbtn.io/status') as response:
        html - response.read()
        print('body response:')
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(type))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
