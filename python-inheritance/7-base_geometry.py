#!/usr/bin/python3
"""create empty class"""


class BaseGeometry:
    """empty class"""
    def area(self):
        """public instance method tocalculate area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integ valid"""

        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
