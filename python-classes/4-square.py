#!/usr/bin/python3
"""next step in square class"""


class Square:
    """Square class with private attribute size"""
    def __init__(self, size=0):
        """Initialize Square with size attribute"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public instance method that returns the current square area."""
        return self.__size * self.__size
