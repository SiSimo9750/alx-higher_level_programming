#!/usr/bin/python3
"""A script that fetches
    https://alx-intranet.hbtn.io/status.
"""

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        RespoContent = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(RespoContent)))
        print("\t- content: {}".format(RespoContent))
        print("\t- utf8 content: {}".format(RespoContent.decode('utf-8')))
