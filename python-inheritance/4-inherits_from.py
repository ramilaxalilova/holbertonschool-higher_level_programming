#!/usr/bin/python3
"""check subclass"""


def inherits_from(obj, a_class):
    """check sub"""
    obj_class = type(obj)
    return issubclass(obj_class, a_class) and obj_class != a_class
