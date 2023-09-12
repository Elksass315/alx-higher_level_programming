#!/usr/bin/python3
""" dictionary description with simple data structure for JSON"""


def class_to_json(obj):
    """dictionary represntation of a simple data structure."""
    return obj.__dict__
