#!/usr/bin/python3

if __name__ == "__main__":
    """print calc"""

    a = 10
    b = 5

    from calculator_1 import add, sub, mul, div

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}\n{} / {} = {}".format(a, b, mul(a, b), a, b, div(a, b)))
