#!/usr/bin/python3
"""Defines rectangle"""


class Rectangle:
    """rectangle"""
    def __init__(self, width=0, height=0):
        """initialize width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """defines width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set value of width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """defines width as private"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be an integer')
        self.__height = value
