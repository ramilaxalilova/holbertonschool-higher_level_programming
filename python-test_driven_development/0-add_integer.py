#!/usr/bin/python3
"""0-add_integer.py and tests/0-add_integer.txt"""


def add_integer(a, b=98):
    """
    Adds two integer
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
