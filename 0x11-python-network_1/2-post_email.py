#!/usr/bin/python3
"""A script that:take URL and sends a POST request
and takes email as a parameter displays the body of the response
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    myUrl = sys.argv[1]
    emailValue = {"email": sys.argv[2]}
    emailData = urllib.parse.urlencode(emailValue).encode("ascii")

    request = urllib.request.Request(myUrl, emailData)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
