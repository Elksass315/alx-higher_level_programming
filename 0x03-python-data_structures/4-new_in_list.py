#!/usr/bin/python3
#4-new_in_list.py

def new_in_list(my_list, idx, element):
    """Replace"""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    l = [x for x in my_list]
    l[idx] = element
    return (l)
