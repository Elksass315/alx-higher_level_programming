#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """print"""
    
    if my_list is None:
        return
    i = len(my_list) - 1

    while i >= 0:
        print("{:d}".format(my_list[i]))
        i = i - 1
