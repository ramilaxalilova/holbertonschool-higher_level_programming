#!/usr/bin/python3
"""Unittest for Base class"""

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """this is class for testing base class"""

    def setUp(self):
        """set up method"""
        Base._Base__nb_objects = 0

    def test_init(self):
        """test init method"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_to_json_string(self):
        """test to_json_string method"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        d1 = {"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}
        d2 = {"id": 6, "x": 7, "y": 8, "width": 9, "height": 10}
        json_list = Base.to_json_string([d1, d2])
        self.assertTrue(type(json_list) is str)
        self.assertCountEqual(json_list, '[{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}, {"id": 6, "x": 7, "y": 8, "width": 9, "height": 10}]')

    def test_save_to_file(self):
        """test save_to_file method"""
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        self.assertTrue(os.path.exists("Base.json"))
        with open("Base.json", "r") as f:
            content = f.read()
            self.assertCountEqual(content, '[{"id": 1}, {"id": 2}]')

    def test_from_json_string(self):
        """test from_json_string method"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        list_dict = Base.from_json_string('[{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}, {"id": 6, "x": 7, "y": 8, "width": 9, "height": 10}]')
        self.assertTrue(type(list_dict) is list)
        self.assertEqual(len(list_dict), 2)
        self.assertEqual(list_dict[0], {"id": 1, "x": 2, "y": 3, "width": 4, "height": 5})
        self.assertEqual(list_dict[1], {"id": 6, "x": 7, "y": 8, "width": 9, "height": 10})

    def test_create(self):
        """test create method"""
        b1 = Base.create(**{"id": 89})
        self.assertEqual(b1.id, 89)
        b2 = Base.create(**{"id": 99, "width": 98})
        self.assertEqual(b2.id, 99)
        self.assertEqual(b2.width, 98)

    def test_load_from_file(self):
        """test load_from_file method"""
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        self.assertEqual(Base.load_from_file(), [])
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        list_objs = Base.load_from_file()
        self.assertTrue(type(list_objs) is list)
        self.assertEqual(len(list_objs), 2)
        self.assertEqual(list_objs[0].id, 1)
        self.assertEqual(list_objs[1].id, 2)

if __name__ == '__main__':
    unittest.main()
