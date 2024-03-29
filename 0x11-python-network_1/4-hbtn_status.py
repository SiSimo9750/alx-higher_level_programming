#!/usr/bin/python3
"""fetches the given link"""
import requests


if __name__ == "__main__":
    myReq = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(myReq.text)))
    print("\t- content: {}".format(myReq.text))
