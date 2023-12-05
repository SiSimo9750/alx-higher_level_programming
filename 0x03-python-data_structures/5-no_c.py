#!/usr/bin/env python3
def no_c(my_string):
    mynew_str = ""
    for i in range(len(my_string)):
        if ord(my_string[i]) == 99 or ord(my_string[i]) == 67:
            continue
        else:
            mynew_str = mynew_str + my_string[i]
    return mynew_str
