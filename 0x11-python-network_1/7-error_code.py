#!/usr/bin/python3
"""Sends a request to a given URL, print the response and Handle HTTP errors.
"""
import sys
import requests


if __name__ == "__main__":
    myUrl = sys.argv[1]

    URLreq = requests.get(myUrl)
    if URLreq.status_code >= 400:
        print("Error code: {}".format(URLreq.status_code))
    else:
        print(URLreq.text)
