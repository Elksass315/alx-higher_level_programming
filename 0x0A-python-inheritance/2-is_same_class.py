#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check  if the object is exactly an instance of the specified class.

    Args:
        obj (any): The obj to check.
        a_class (type): The class to match to.
    Returns:
        If from the same class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
