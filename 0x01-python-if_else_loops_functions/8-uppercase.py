#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        ch = ord(str[i])
        if 96 < ch < 123:
            ch = ch - 32
        print("{:c}".format(ch), end="")
    print()
