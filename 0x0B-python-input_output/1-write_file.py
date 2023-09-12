#!/usr/bin/python3
"""file writing func"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): file name to be write.
        text (str): text to be write in the file.
    Returns:
        The num of characters.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
