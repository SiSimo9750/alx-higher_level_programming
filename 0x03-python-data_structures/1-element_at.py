#!/usr/bin/env python3
def element_at(my_list, idx):
    if len(my_list) <= idx or idx < 0:
        return None
    else:
        return my_list[idx]
