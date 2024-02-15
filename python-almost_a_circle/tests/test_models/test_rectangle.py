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

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_update_no_args(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (42) 1/2 - 2/4")

    def test_update_args_none_id(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(None)
        self.assertEqual(str(r), "[Rectangle] (1) 1/2 - 2/4")

    def test_update_args_id(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(24)
        self.assertEqual(str(r), "[Rectangle] (24) 1/2 - 2/4")

    def test_update_args_id_width(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(24, 10)
        self.assertEqual(str(r), "[Rectangle] (24) 1/2 - 10/4")

    def test_update_args_id_width_height(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(24, 10, 20)
        self.assertEqual(str(r), "[Rectangle] (24) 1/2 - 10/20")

    def test_update_args_id_width_height_x(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(24, 10, 20, 30)
        self.assertEqual(str(r), "[Rectangle] (24) 30/2 - 10/20")

    def test_update_args_id_width_height_x_y(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(24, 10, 20, 30, 40)
        self.assertEqual(str(r), "[Rectangle] (24) 30/40 - 10/20")

    def test_update_args_too_many_args(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(10, 10, 10, 10, 10, 50, 60)
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_update_kwargs_none_id(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(id=None)
        self.assertEqual(str(r), "[Rectangle] (1) 1/2 - 2/4")

    def test_update_kwargs_id(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(id=24)
        self.assertEqual(str(r), "[Rectangle] (24) 1/2 - 2/4")

    def test_update_kwargs_id_width(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(width=10, id=24)
        self.assertEqual(str(r), "[Rectangle] (24) 1/2 - 10/4")

    def test_update_kwargs_id_width_height(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(width=10, id=24, height=20)
        self.assertEqual(str(r), "[Rectangle] (24) 1/2 - 10/20")

    def test_update_kwargs_id_width_height_x(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(width=10, id=24, x=30, height=20)
        self.assertEqual(str(r), "[Rectangle] (24) 30/2 - 10/20")

    def test_update_kwargs_id_width_height_x_y(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(y=40, width=10, id=24, x=30, height=20)
        self.assertEqual(str(r), "[Rectangle] (24) 30/40 - 10/20")

    def test_update_kwargs_too_many_args(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(y=10, width=10, id=10, x=10, height=10, betty="holberton")
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")

    def test_update_kwargs_mixed_too_many_args(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(y=10, width=10, betty="holberton", id=10, x=10, height=10)
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")

    def test_update_kwargs_args_before(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(42, 42, 42, y=10, x=10)
        self.assertEqual(str(r), "[Rectangle] (42) 1/2 - 42/42")

    def test_update_kwargs_not_all_mixed(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(y=10, x=10, height=10)
        self.assertEqual(str(r), "[Rectangle] (42) 10/10 - 2/10")

    def test_update_kwargs_only_wrong_keys(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(betty="holberton", holberton="betty")
        self.assertEqual(str(r), "[Rectangle] (42) 1/2 - 2/4")

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_str_print(self):
        expected = "[Rectangle] (42) 1/3 - 2/4"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            print(Rectangle(2, 4, 1, 3, 42), end='')
            self.assertEqual(output.getvalue(), expected)

    def test_str_str_method(self):
        expected = "[Rectangle] (98) 3/1 - 4/2"
        self.assertEqual(Rectangle(4, 2, 3, 1, 98).__str__(), expected)

    def test_str_str(self):
        expected = "[Rectangle] (1) 0/0 - 4/4"
        self.assertEqual(str(Rectangle(4, 4)), expected)

    def test_str_str_method_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4).__str__(42)
