#!/usr/bin/python3

def safe_print_integer(value):
    """print integer

    args:
        value (int): the int to be print

    Returns:
        if any error occurs - False.
        else - True.
    """

    try:
        print("{:d}".format(value))
        return(True)
    except(TypeError, ValueError):
        return(False)
