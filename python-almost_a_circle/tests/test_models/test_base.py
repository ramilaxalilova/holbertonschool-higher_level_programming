#!/usr/bin/python3
"""Unittest for base({..]) after task 1"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests `Base` class."""

    @classmethod
    def setUpClass(cls):
        """Alerts user to any instances of tested classes or subclasses not
        already cleaned up. """
        b_obj = Base._Base__nb_objects
        b_tobj = Base._Base__true_nb_objects
        b_ids = Base._Base__assigned_ids
        if b_obj > 1:
            print('testBase: previous Base counter not reset,' +
                  'now at: {}'.format(b_obj))
        if b_tobj > 1:
            print('testBase: previous total Base counter not reset,' +
                  'now at: {}'.format(b_tobj))
        if len(b_ids) > 0:
            print('testBase: previous Base ids still potentially in' +
                  'use: {}'.format(b_ids))

    def tearDown(self):
        """Reinitializes obejct iterator and set of assigned ids."""
        b_ids = Base._Base__assigned_ids
        Base._Base__nb_objects = 0
        b_obj = Base._Base__nb_objects
        Base._Base__true_nb_objects = 0
        b_tobj = Base._Base__true_nb_objects
        b_ids.clear()
        if b_obj > 1:
            print('testBase: Base counter not reset, now at: {}'.format(b_obj))
        if b_tobj > 1:
            print('testBase: total Base counter not reset,' +
                  ' now at: {}'.format(b_tobj))
        if len(b_ids) > 0:
            print('testBase: Base ids still potentially in' +
                  'use: {}'.format(b_ids))

    def test_id(self):
        """Task 1. Base class"""
        self.assertRaises(ValueError, Base, 0)
        self.assertRaises(ValueError, Base, -5)
        b1 = Base(2)
        self.assertEqual(b1.id, 2)
        self.assertEqual(b1.serial, 1)
        b2 = Base()
        self.assertEqual(b2.id, 1)
        self.assertEqual(b2.serial, 2)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        self.assertEqual(b3.serial, 3)
        b4 = Base(2)
        self.assertEqual(b1.id, 2)
        self.assertEqual(b1.serial, 1)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b3.serial, 3)
        self.assertEqual(b4.id, 2)
        self.assertEqual(b4.serial, 4)

    def test_to_json_string(self):
        """15. Dictionary to JSON string"""
        d_list = [{'id': 10}, {'id': 15}]
        self.assertEqual(Base.to_json_string(d_list),
                         '[{"id": 10}, {"id": 15}]')
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')
        lst = [2, 3, 4]
        self.assertEqual(Base.to_json_string(lst), '[2, 3, 4]')
        self.assertRaises(TypeError, Base.to_json_string)
        d_list2 = [{'id': 20}]
        self.assertRaises(TypeError, Base.to_json_string, d_list, d_list2)

    def test_save_to_file(self):
        """16. JSON string to file"""
        pass

    def test_from_json_string(self):
        """17. JSON string to dictionary"""
        a = Base.from_json_string('[{"id": 10}, {"id": 15}]')
        self.assertEqual(a, [{'id': 10}, {'id': 15}])
        b = Base.from_json_string('')
        self.assertEqual(b, [])
        c = Base.from_json_string(None)
        self.assertEqual(c, [])
        self.assertRaises(TypeError, Base.from_json_string)
        self.assertRaises(TypeError, Base.from_json_string, a, b)

    def test_create(self):
        """18. Dictionary to Instance"""

        pass

    def test_load_from_file(self):
        """19. File to instances """
        pass

if __name__ == '__main__':
    unittest.main()