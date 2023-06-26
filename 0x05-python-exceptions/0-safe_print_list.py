#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x  elememts in the list.
    Args:
        my_list (list): list to be print from.
        x (int): The number of elements.

    Returns:
        numper of elements have been printed
    """
    r = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (r)
