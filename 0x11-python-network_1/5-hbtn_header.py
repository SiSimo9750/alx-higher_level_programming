#!/usr/bin/python3
"""Print the X-Request-Id header variable of a request to myURL
"""
import sys
import requests


if __name__ == "__main__":
    myUrl = sys.argv[1]

    URLrespo = requests.get(myUrl)
    print(URLrespo.headers.get("X-Request-Id"))
