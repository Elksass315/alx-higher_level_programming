#!/usr/bin/python3
"""JSON to string function."""
import json


def from_json_string(my_str):
    """returns the string representation of a JASON object"""
    return json.loads(my_str)
