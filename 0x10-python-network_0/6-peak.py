#!/usr/bin/python3
"""script for finding peak in list of ints, interview prep
"""

"""
    THOUGHT PROCESS
        it is not sorted, so sorting would take n(log(n))
            -> not worth sorting
        looping through and keeping track of max (brute force)
            -> O(n)

        possibly looping from each end reducing to 1/2 run time
            -> still O(n)
"""


peak(list_of_integers):
    """ firnd peak"""
    if not list_of_integers:
        return None

    list_length = len(list_of_integers)

    # If the list has only one element, return it
    if list_length == 1:
        return list_of_integers[0]

    # Check the first and last elements
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]

    # Check the rest of the list
    for i in range(1, list_length - 1):
        if list_of_integers[i] >= list_of_integers[i - 1] and list_of_integers[i] >= list_of_integers[i + 1]:
            return list_of_integers[i]

    return None
