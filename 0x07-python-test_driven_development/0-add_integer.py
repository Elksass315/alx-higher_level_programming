#!/usr/bin/python3
"""0. Integers addition"""


def add_integer(a, b=98):
    """function that adds 2 integers.
    
    args: a (int) frist number.
          b (int) 2nd number.
    """

    typeList = [int, float]
    if not type(a) in typeList:
        raise ValueError("a must be an integer")
    if  not type(b) in typeList:
        raise ValueError("b must be an integer")
    return int(a) + int(b)
