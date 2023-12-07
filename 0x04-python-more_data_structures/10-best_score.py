#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_value = 0
        for i in a_dictionary:
            if a_dictionary[i] > max_value:
                max_value = a_dictionary[i]
                max_key = i
        return max_key
