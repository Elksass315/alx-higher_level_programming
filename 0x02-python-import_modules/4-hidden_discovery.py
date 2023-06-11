#!/usr/bin/python3

if __name__ == "__main__":
    """print"""

    import hidden_4 as h

    n = dir(h)
    for i in n:
        if i[:2] != "__":
            print(i)
