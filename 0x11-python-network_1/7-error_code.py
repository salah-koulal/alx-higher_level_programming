#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL and displays
the body of the response."""

import requests
import sys

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    sttus_code = res.status_code
    if sttus_code >= 400:
        print("Error code: {}".format(sttus_code))
    else:
        print(res.text)
