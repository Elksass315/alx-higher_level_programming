#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers.

    args:
        my_list (list): list of num to be print.
        x (int): numper of elements to print.

    Returns:
        The number of elements printed.
    """

    r = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            r += 1
        except(ValueError, TypeError):
            continue
    print("")
    return r
