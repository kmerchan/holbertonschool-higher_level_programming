#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """contains test functions for max_integer function"""

    def test_area(self):
        """tests successful cases of max_integer"""
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 1, 3, 3, 3, 6, 8, 8]), 8)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([1, 2, 3, 4, 3, 2, 1]), 4)

    def test_errors(self):
        """tests errors raised by incorrect type arguments"""
        self.assertRaises(Exception, max_integer, ["string", 1.73, 25, {2}])

    def test_empty(self):
        """tests errors if argument is none"""
        self.assertIsNone(max_integer())
