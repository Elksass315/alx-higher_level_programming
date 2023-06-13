#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    new = ""
    c_list = ['c', 'C']

    for i in my_string:
        if i not in c_list:
            new = new + i

    return new
