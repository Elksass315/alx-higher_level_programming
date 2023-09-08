#!/usr/bin/python3
"""Write a function that prints a text with 2
    new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :

    args:
        text (string): the text.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    X = 0
    while X < len(text) and text[X] == ' ':
        X += 1

    while X < len(text):
        print(text[X], end="")
        if text[X] == "\n" or text[c] in ".?:":
            if text[X] in ".?:":
                print("\n")
            X += 1
            while X < len(text) and text[X] == ' ':
                X += 1
            continue
        X += 1

