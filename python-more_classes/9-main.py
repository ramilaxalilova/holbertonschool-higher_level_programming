#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square("2")
print("{} / {}".format(my_square.width, my_square.height))
print(my_square)
