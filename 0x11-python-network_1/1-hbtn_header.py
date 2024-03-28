#!/usr/bin/python3
"""A script thats displays the X-Request-Id header of a request to an URL
"""
import sys
import urllib.request

if __name__ == "__main__":
    myUrl = sys.argv[1]

    myUrlRequest = urllib.request.Request(myUrl)
    with urllib.request.urlopen(myUrlRequest) as response:
        print(dict(response.headers).get("X-Request-Id"))
