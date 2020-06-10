#!/usr/bin/python3
"""unittest for Rectangle class"""


import unittest

from models.rectangle import Rectangle

class TestBaseInit(unittest.TestCase):
    """testing functions for Rectangle class"""

    def test_a_rectangle_instantiation(self):
        """test initialization of rectangle instance"""
        r1 = Rectangle(11, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 11)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(5, 67, 55, 81)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 67)
        self.assertEqual(r2.x, 55)
        self.assertEqual(r2.y, 81)
        r3 = Rectangle(24, 89, 45, 16, 73)
        self.assertEqual(r3.id, 73)
        self.assertEqual(r3.width, 24)
        self.assertEqual(r3.height, 89)
        self.assertEqual(r3.x, 45)
        self.assertEqual(r3.y, 16)
        r4 = Rectangle(60, 200)
        self.assertEqual(r4.id, 3)
        self.assertEqual(r4.width, 60)
        self.assertEqual(r4.height, 200)
        self.assertEqual(r4.x, 0)
        self.assertEqual(r4.y, 0)

    def test_errors(self):
        """tests errors raised during initialization"""
        self.assertRaises(TypeError, Rectangle, [width="9", height="5"])
        self.assertRaises(TypeError, Rectangle, [width=[8], height=[2]])
        self.assertRaises(TypeError, Rectangle, [width=2.7159, height=3.14159])
        self.assertRaises(TypeError, Rectangle, [width={7}, height={13}])
        self.assertRaises(TypeError, Rectangle, [width=(6,), height=(44,)])
        self.assertRaises(TypeError, Rectangle, [width=None, height=None])
        self.assertRaises(ValueError, Rectangle, [width=0, height=0])
        self.assertRaises(ValueError, Rectangle, [width=-8, height=2])
        self.assertRaises(ValueError, Rectangle, [width=7, height=-13])

#        self.assertRaises(TypeError, Rectangle.__init__, [4, 7, "9", "5"])
 #       self.assertRaises(TypeError, Rectangle.__init__, [3, 9, [8], [2]])
  #      self.assertRaises(TypeError, Rectangle.__init__, [1, 1, 2.712, 3.14159])
   #     self.assertRaises(TypeError, Rectangle.__init__, [200, 576, {7}, {13}])
    #    self.assertRaises(TypeError, Rectangle.__init__, [5, 4, (6,), (44,)])
     #   self.assertRaises(TypeError, Rectangle.__init__, [7, 8, None, None])
      #  self.assertRaises(ValueError, Rectangle.__init__, [8, 2, -3, 5])
       # self.assertRaises(ValueError, Rectangle.__init__, [1, 49, 7, -13])
