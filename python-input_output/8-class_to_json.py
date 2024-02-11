#!/usr/bin/python3
"""function class tojson"""


def class_to_json(obj: object):
    """Class to Json"""
    return obj.__dict__
