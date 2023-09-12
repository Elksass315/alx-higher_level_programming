#!/usr/bin/python3
"""file appinding func"""


def write_file(filename="", text=""):
    """append a string to a UTF8 text file.

    Args:
        filename (str): file name to be write.
        text (str): text to be appended in the file.
    Returns:
        The num of characters.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
