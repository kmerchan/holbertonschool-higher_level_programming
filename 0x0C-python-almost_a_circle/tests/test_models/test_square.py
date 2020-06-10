#!/usr/bin/python3
"""unittest for Rectangle class"""


import unittest
import pep8

from models.square import Square

class TestSquare(unittest.TestCase):
    """testing functions for Square class"""

    def test_a_square_instantiation(self):
        """test initialization of square instance"""
        r1 = Square(11)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 11)
        self.assertEqual(r1.height, 11)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Square(5, 55, 81)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 55)
        self.assertEqual(r2.y, 81)
        r3 = Square(24, 45, 16, 73)
        self.assertEqual(r3.id, 73)
        self.assertEqual(r3.width, 24)
        self.assertEqual(r3.height, 24)
        self.assertEqual(r3.x, 45)
        self.assertEqual(r3.y, 16)
        r4 = Square(60)
        self.assertEqual(r4.id, 3)
        self.assertEqual(r4.width, 60)
        self.assertEqual(r4.height, 60)
        self.assertEqual(r4.x, 0)
        self.assertEqual(r4.y, 0)

#    def test_errors(self):
 #       """tests errors raised during initialization"""
  #      r1 = Rectangle(1, 2, 3, 4)
   #     self.assertRaises(TypeError, self.r1.__init__, ["9", "5"])
  #      self.assertRaises(TypeError, self.r1.__init__, [[8], [2]])
   #     self.assertRaises(TypeError, self.r1.__init__, [2.7159, 3.14159])
    #    self.assertRaises(TypeError, self.r1.__init__, [{7}, {13}])
     #   self.assertRaises(TypeError, self.r1.__init__, [(6,), (44,)])
      #  self.assertRaises(TypeError, self.r1.__init__, [None, None])
       # self.assertRaises(ValueError, self.r1.__init__, [0, 0])
        #self.assertRaises(ValueError, self.r1.__init__, [-8, 2])
        #self.assertRaises(ValueError, self.r1.__init__, [7, -13])

#        self.assertRaises(TypeError, Rectangle.__init__, [4, 7, "9", "5"])
 #       self.assertRaises(TypeError, Rectangle.__init__, [3, 9, [8], [2]])
  #      self.assertRaises(TypeError, Rectangle.__init__, [1, 1, 2.712, 3.14159])
   #     self.assertRaises(TypeError, Rectangle.__init__, [200, 576, {7}, {13}])
    #    self.assertRaises(TypeError, Rectangle.__init__, [5, 4, (6,), (44,)])
     #   self.assertRaises(TypeError, Rectangle.__init__, [7, 8, None, None])
      #  self.assertRaises(ValueError, Rectangle.__init__, [8, 2, -3, 5])
       # self.assertRaises(ValueError, Rectangle.__init__, [1, 49, 7, -13])

    def test_pep8(self):
        """test that code follows pep8 style guidelines"""
        pep8style = pep8.StyleGuide(quiet=True)
