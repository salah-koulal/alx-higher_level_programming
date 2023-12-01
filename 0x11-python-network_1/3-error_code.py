#!/usr/bin/python3
""" Script takes in a URL, sends a request to the URL
and displays the body of the response
(decoded in utf-8)
"""
import urllib.request as ulib
import sys
import urllib.error

if __name__ == "__main__":
    try:
        with ulib.urlopen(sys.argv[1]) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
