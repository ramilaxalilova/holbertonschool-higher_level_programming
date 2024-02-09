#!/usr/bin/python3
"""create empty class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """create square based on rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """print string"""
        return f"[Square] {self.__size}/{self.__size}"
