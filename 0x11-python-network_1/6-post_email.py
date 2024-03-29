#!/usr/bin/python3
"""Sends a POST request to a URL, email and print the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    myUrl = sys.argv[1]
    emailValue = {"email": sys.argv[2]}

    URLreq = requests.post(myUrl, data=emailValue)
    print(URLreq.text)
