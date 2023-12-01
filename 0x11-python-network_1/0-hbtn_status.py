#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request as ulib

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with ulib.urlopen(url) as response:
        content = response.read()
        dec_content = content.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(dec_content))
