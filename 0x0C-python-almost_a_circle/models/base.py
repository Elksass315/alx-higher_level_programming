#!/usr/bin/python3
"""the “base” of all other classes in this project."""
import json


class Base:
    """The goal of it is to manage id attribute in all of my
    future classes and to avoid duplicating
    the same code (by extension, same bugs)

    Private Attributes:
        __nb_object (int): Number of uninstantiated instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor

        Args:
            id (int): new base id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation of list_dictionaries

            args:
                list_dictionaries (list): list of dictionaries to be JSON
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
