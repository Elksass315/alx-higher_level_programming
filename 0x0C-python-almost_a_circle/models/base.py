#!/usr/bin/python3
"""the “base” of all other classes in this project."""
import json
import csv
import turtle


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

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set.

        Args:
            **dictionary can be thought of as a double pointer to a dictionary
        """
        if dictionary != {}:
            if cls.__name__ == "Rectangle":
                x = cls(1, 1)
            else:
                x = cls(1)
            x.update(**dictionary)
            return x

    @classmethod
    def load_from_file(cls):
        """returns a list of instances

            return:
                If the file doesn’t exist, return an empty list
                Otherwise, return a list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                listOfDict = Base.from_json_string(f.read())
                return [cls.create(**i) for i in listOfDict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serialization in CSV.
            Format of the CSV:
                Rectangle: <id>,<width>,<height>,<x>,<y>
                Square: <id>,<size>,<x>,<y>

        Args:
            list_objs (list): list of obj.
        """
        name = cls.__name__ + ".csv"
        with open(name, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field = ["id", "width", "height", "x", "y"]
                else:
                    field = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=field)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        name = cls.__name__ + ".csv"
        try:
            with open(name, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    field = ["id", "width", "height", "x", "y"]
                else:
                    field = ["id", "size", "x", "y"]
                dic = csv.DictReader(f, fieldnames=field)
                dic = [dict([k, int(v)] for k, v in d.items())for d in dic]
                return [cls.create(**d) for d in dic]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7132c")
        turt.pensize(7)
        turt.shape("turtle")

        turt.color("#aaaaff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5efd8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
