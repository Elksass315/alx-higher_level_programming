#!/usr/bin/python3
"""Defines an inherited checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited from class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
         if the object is an instance of a class that inherited
         (directly or indirectly)
         from the specified class  - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
