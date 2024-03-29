#!/usr/bin/python3
"""Display the 10 recent commits on a entred GitHub repository.
"""
import sys
import requests


if __name__ == "__main__":
    myUrl = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    myReq = requests.get(myUrl)
    commits = myReq.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
