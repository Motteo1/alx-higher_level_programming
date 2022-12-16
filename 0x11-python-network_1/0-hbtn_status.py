#!/usr/bin/python3
"""
fetch https://intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopn('https://intranet.hbtn.io/status') as response:
        html - response.read()
        print('body response:')
