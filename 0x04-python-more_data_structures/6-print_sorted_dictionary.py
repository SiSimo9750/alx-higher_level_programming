#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary)
    for i in sorted_keys:
        print(i, ": ", a_dictionary[i], sep="")
