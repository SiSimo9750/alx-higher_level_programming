#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_new_list = my_list[:]
    for i in range(len(my_new_list)):
        if my_new_list[i] == search:
            my_new_list[i] = replace
    return my_new_list
