#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

a = 1
b= 2

if __name__ == "__main__":
    print(f"{a} + {b} = {add(a, b)}")
