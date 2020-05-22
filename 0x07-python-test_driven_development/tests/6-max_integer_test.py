#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_area(self):
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 1, 3, 3, 3, 6, 8, 8]), 8)
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_errors(self):
        self.assertRaises(Exception, max_integer, ["string", 1.73, 25, {2}])

    def test_empty(self):
        self.assertIsNone(max_integer())
