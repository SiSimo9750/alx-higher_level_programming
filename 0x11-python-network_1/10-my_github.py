#!/usr/bin/python3
"""Uses GitHub API to print GitHub ID based on given credentials.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    myReq = requests.get("https://api.github.com/user", auth=auth)
    print(myReq.json().get("id"))
