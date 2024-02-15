#!/usr/bin/python3
"""
A module that test differents behaviors
of the Base class
"""
from unittest import TestCase, mock
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(TestCase):
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

        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.id, 11)
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

    