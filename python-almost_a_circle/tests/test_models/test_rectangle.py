#!/usr/bin/python3
"""
A module that test differents behaviors
of the Base class
"""
import unittest
from unittest import mock
from io import StringIO
import json
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    A class to test the Rectangle Class
    """

    def test_rectangle_subclass(self):
        """
        Test if Rectangle class inherit from
        Base class
        """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_parameters(self):
        """
        Test parameters for Rectangle class
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.id, 11)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.id, 12)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

        with self.assertRaises(TypeError):
            r4 = Rectangle()

    def test_string(self):
        """
        Test string parameters for a
        Rectangle class
        """
        with self.assertRaises(TypeError):
            Rectangle('C', 'Python')

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_value_errors(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area_basic(self):
        self.assertEqual(Rectangle(2, 4).area(), 8)

    def test_area_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4).area(42)

    def test_display_basic(self):
        with mock.patch('sys.stdout', new=StringIO()) as output:
            Rectangle(2, 4).display()
            self.assertEqual(output.getvalue(), '##\n##\n##\n##\n')

    def test_display_with_x(self):
        with mock.patch('sys.stdout', new=StringIO()) as output:
            Rectangle(2, 4, 2).display()
            self.assertEqual(output.getvalue(), '  ##\n  ##\n  ##\n  ##\n')

    def test_display_with_y(self):
        with mock.patch('sys.stdout', new=StringIO()) as output:
            Rectangle(2, 4, 0, 2).display()
            self.assertEqual(output.getvalue(), '\n\n##\n##\n##\n##\n')

    def test_display_with_x_y(self):
        with mock.patch('sys.stdout', new=StringIO()) as output:
            Rectangle(2, 4, 2, 2).display()
            self.assertEqual(output.getvalue(), '\n\n  ##\n  ##\n  ##\n  ##\n')

    def test_display_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4).display(42)

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1, 0, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_update(self):
        r44 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(str(r44), "[Rectangle] (1) 10/10 - 10/10")
        r44.update(89)
        self.assertEqual(str(r44), "[Rectangle] (89) 10/10 - 10/10")
        r44.update(89, 2)
        self.assertEqual(str(r44), "[Rectangle] (89) 10/10 - 2/10")
        r44.update(89, 2, 3)
        self.assertEqual(str(r44), "[Rectangle] (89) 10/10 - 2/3")
        r44.update(89, 2, 3, 4)
        self.assertEqual(str(r44), "[Rectangle] (89) 4/10 - 2/3")
        r44.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r44), "[Rectangle] (89) 4/5 - 2/3")
        r44.update(height=1)
        self.assertEqual(str(r44), "[Rectangle] (89) 4/5 - 2/1")
        r44.update(width=1, x=2)
        self.assertEqual(str(r44), "[Rectangle] (89) 2/5 - 1/1")
        r44.update(y=1, width=2, x=3, id=44)
        self.assertEqual(str(r44), "[Rectangle] (44) 3/1 - 2/1")
        r44.update(45, 10, y=0, width=10, x=4, id=89)
        self.assertEqual(str(r44), "[Rectangle] (45) 3/1 - 10/1")

        with self.assertRaises(TypeError):
            r44.update(89, 2, 3, 'h', 5)
        with self.assertRaises(TypeError):
            r44.update(89, 'h', 3, 2, 5)
        with self.assertRaises(TypeError):
            r44.update(y=1, width='h', x=3, id=44)

    def test_to_dict_rect(self):
        r45 = Rectangle(10, 2, 1, 9, 1)
        r46 = Rectangle(11, 10, 10, 10, 10)
        r45_dictionary = r45.to_dictionary()
        self.assertTrue(type(r45_dictionary) is dict)
        self.assertIn('id', r45_dictionary)
        self.assertIn('width', r45_dictionary)
        self.assertIn('height', r45_dictionary)
        self.assertIn('x', r45_dictionary)
        self.assertIn('y', r45_dictionary)
        self.assertEqual(r45_dictionary['id'], 1)
        self.assertEqual(r45_dictionary['width'], 10)
        self.assertEqual(r45_dictionary['height'], 2)
        self.assertEqual(r45_dictionary['x'], 1)
        self.assertEqual(r45_dictionary['y'], 9)
        self.assertEqual(len(r45_dictionary), 5)
        r46.update(**r45_dictionary)
        self.assertEqual(str(r46), "[Rectangle] (1) 1/9 - 10/2")
        r46_dictionary = r46.to_dictionary()
        self.assertEqual(r45_dictionary, r46_dictionary)

    def test_create(self):
        rect_dict = {'id': 89, 'width': 10, 'height': 20, 'x': 2, 'y': 3}
        rect = Rectangle.create(**rect_dict)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", mode="r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", mode="r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file(self):
        rect = Rectangle(1, 2)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as file:
            content = json.load(file)
            self.assertEqual(content, [rect.to_dictionary()])


if __name__ == '__main__':
    unittest.main()