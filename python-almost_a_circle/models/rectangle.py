#!/usr/bin/python3
"""ractangle from base"""
from models.base import Base


class Rectangle(Base):
    """RECTANGLE CLASS"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @property
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @property
    def height(self, value):
        self.__height = height

    @property
    def x(self):
        return self.__x

    @property
    def x(self, value):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @property
    def y(self, value):
        self.__y = value
