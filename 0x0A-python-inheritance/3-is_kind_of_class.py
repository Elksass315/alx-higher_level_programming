#!/usr/bin/python3
"""func bject is an instance of,
or if the object is an instance of a class that inherited"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): an obj.
        a_class (type): The class to match the type of obj to.
    Returns:
         if the object is an instance of,
         or if the object is an instance of a class
         that inherited from, the specified class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
