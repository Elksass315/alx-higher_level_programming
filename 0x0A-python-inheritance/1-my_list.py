#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """sorted printing for a list"""

    def print_sorted(self):
        """Print sorted list (ascending sort)"""
        print(sorted(self))
