#!/usr/bin/python3
"""create empty class"""


class BaseGeometry:
    """empty class"""
    def area(self):
        """public instance method tocalculate area"""
        raise Exception('area() is not implemented')
