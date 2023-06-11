#!/usr/bin/python3

if __name__ == "__main__":
    """print"""

    from sys import argv as v

    x = 0
    for i in range(len(v) - 1):
        x += int(v[i+1])
    print("{}".format(x))
