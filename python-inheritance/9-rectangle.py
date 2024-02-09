#!/usr/bin/python3
"""create empty class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """create rectangle based on parentclass"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculate area"""
        return (self.__width * self.__height)

    def __str__(self):
        """print string"""
        return f"[Rectangle] {self.__width}/{self.__height}"
