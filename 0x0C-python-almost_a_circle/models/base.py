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

    @classmethod
    def save_to_file(cls, list_objs):
        """rites the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        f = cls.__name__ + ".json"
        with open(f, "w") as jf:
            if list_objs is None:
                jf.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jf.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return JSON string.

        Args:
            json_string: is a string representing a list of dictionaries.
        Returns:
            If If json_string is None or empty, return an empty list
            Otherwise, return the list represented by json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)


