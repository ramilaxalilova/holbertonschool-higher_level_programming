#!/usr/bin/python3
"""issame"""


def is_same_class(obj, a_class):
    """check type"""
    if type(obj) is a_class:
        return True
    return False
