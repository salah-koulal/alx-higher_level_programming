#!/usr/bin/python3
""" Script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    url = "https://api.github.com/user"
    info = {"login": sys.argv[1]}
    response = requests.get(url, auth=(username, passwd), params=info).json()
    if response.get("id") is not None:
        print("{}".format(response.get("id")))
    else:
        print("None")
