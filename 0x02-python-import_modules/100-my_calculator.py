#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys as s
    from sys import argv as v

    if len(v) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        s.exit(1)

    o = {"+": add, "-": sub, "*": mul, "/": div}
    if v[2] not in list(o.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        s.exit(1)

    a = int(v[1])
    b = int(v[3])
    print("{} {} {} = {}".format(a, v[2], b, o[v[2]](a, b)))
