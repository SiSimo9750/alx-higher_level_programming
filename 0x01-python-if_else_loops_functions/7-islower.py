#!/usr/bin/python3
def islower(c):
    i = ord(c)
    if 96 < i < 123:
        return True
    elif i < 0:
        return False
