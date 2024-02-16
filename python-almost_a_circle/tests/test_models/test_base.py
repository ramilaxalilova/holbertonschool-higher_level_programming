#!/usr/bin/python3
"""test differents conditionsof the Base class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """test class for base case"""

    def test_id_as_positive(self):
        """test for pos id"""

        base_instance = Base(115)
        self.assertEqual(base_instance.id, 115)
        base_instance = Base(67)
        self.assertEqual(base_instance.id, 67)

    def test_id_as_negative(self):
        """test for negative id"""

        base_instance = Base(-91)
        self.assertEqual(base_instance.id, -91)
        base_instance = Base(-4)
        self.assertEqual(base_instance.id, -4)

    def test_id_as_none(self):
        """test for none id"""

        base_instance = Base()
        self.assertEqual(base_instance.id, 1)
        base_instance = Base(None)
        self.assertEqual(base_instance.id, 2)

    def test_string_id(self):
        base_instance = Base('SMTHNG')
        self.assertEqual(base_instance.id, 'SMTHNG')
        base_instance = Base('ANYTHNG')
        self.assertEqual(base_instance.id, 'ANYTHNG')

    def test_to_json_string(self):
        """test json sstring"""
        rect_instance = Rectangle(10, 7, 2, 8, 70)
        rect_data = rect_instance.to_dictionary()
        json_data = Base.to_json_string([rect_data])
        self.assertEqual(type(json_data), str)

    def test_to_json_string(self):
        """tests functionality"""

        rect_data = {'id': 31, 'x': 14, 'y': 11, 'width': 3, 'height': 3}
        json_data = Base.to_json_string([rect_data])

        self.assertTrue(isinstance(rect_data, dict))
        self.assertTrue(isinstance(json_data, str))
        self.assertCountEqual(
            json_data,
            '{["id": 31, "x": 14, "y": 11, "width": 3, "height": 3]}'
        )

    def test_from_json_string(self):
        """check from_json_string"""
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]  # list dict
        json_list_input = Rectangle.to_json_string(list_input)  # str list dict
        list_output = Rectangle.from_json_string(json_list_input)  # list dict
        self.assertTrue(list_input == list_output)

    def test_wrong_save_to_file(self):
        """
        Test the save_to_file method
        """
        with self.assertRaises(AttributeError) as msg:
            Base.save_to_file([Base(1), Base(2)])

        self.assertEqual(
             "'Base' object has no attribute 'to_dictionary'",
             str(msg.exception)
        )

if __name__ == "__main__":
    unittest.main()