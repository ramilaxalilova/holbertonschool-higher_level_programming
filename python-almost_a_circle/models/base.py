#!/usr/bin/python3
"""create base class"""
import json
import os.path
import turtle


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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation"""

        filename = f"{cls.__name__}.json"

        with open(filename, mode="w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dlists = [o.to_dictionary() for o in list_objs]
                f.write(cls.to_json_string(dlists))
        f.close()

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Square':
            dummy = cls(3)

        if cls.__name__ == 'Rectangle':
            dummy = cls(3, 3)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """file to instances"""
        if not os.path.exists(cls.__name__ + ".json"):
            return []
        with open(cls.__name__ + ".json", "r") as file:
            stuff = cls.from_json_string(file.read())
        return [cls.create(**index) for index in stuff]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw the objects with Turtle Graphics
        """
        new_window = turtle.Screen()
        new_window.bgcolor("white")
        new_window.title("Made by holbie")
        new_turtle = turtle.Turtle()

        for rectangle in list_rectangles:
            new_turtle.color("Violet", "blue")
            new_turtle.begin_fill()
            dic = rectangle.to_dictionary()
            new_turtle.penup()
            new_turtle.setpos(dic["x"], dic["y"])
            new_turtle.pendown()
            for x in range(0, 2):
                new_turtle.forward(dic["height"])
                new_turtle.right(90)
                new_turtle.forward(dic["width"])
                new_turtle.right(90)
            new_turtle.end_fill()

        for square in list_squares:
            new_turtle.color("Red", "Green")
            new_turtle.begin_fill()
            dic = square.to_dictionary()
            new_turtle.penup()
            new_turtle.setpos(dic["x"], dic["y"])
            new_turtle.pendown()
            for size in range(0, 4):
                new_turtle.forward(dic["size"])
                new_turtle.right(90)
            new_turtle.end_fill()
        turtle.done()