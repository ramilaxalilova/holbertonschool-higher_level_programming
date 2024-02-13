#!/usr/bin/python3
"""create base class"""
import json


class Base:
    """create class with private attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """..."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
