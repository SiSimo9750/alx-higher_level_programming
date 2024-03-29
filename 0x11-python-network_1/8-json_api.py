#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter
"""
import sys
import requests


if __name__ == "__main__":
    EntredLetter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": EntredLetter}

    myReq = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        myRes = myReq.json()
        if myRes == {}:
            print("No result")
        else:
            print("[{}] {}".format(myRes.get("id"), myRes.get("name")))
    except ValueError:
        print("Not a valid JSON")
