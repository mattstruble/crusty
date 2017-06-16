#!/usr/bin/env python

# Copyright (c) 2017 Matt Struble. All Rights Reserved. 
#
# Use is subject to license terms.
#
# Author: Matt Struble
# Date: Jun. 15 2017
from unittest import TestCase
from crusty.util.enum import Enum

class testEnum(Enum):
    A = 0
    B = 1
    C = 2
    D = 5
    
class EnumTestCase(TestCase):
    def setUp(self):
        self.inline = Enum('Test', 'A', 'B', 'C', D=5)
        self.enum = testEnum
        
    def test_init(self):
        self.assertEqual(self.enum.A, 0)
        self.assertEqual(self.enum.B, 1)
        self.assertEqual(self.enum.C, 2)
        self.assertEqual(self.enum.D, 5)
        
        self.assertEqual(self.inline.A, 0)
        self.assertEqual(self.inline.B, 1)
        self.assertEqual(self.inline.C, 2)
        self.assertEqual(self.inline.D, 5)
        
    def test_instance(self):
        self.assertIn(self.inline.A, self.inline)
        self.assertIn(self.enum.A, self.enum)
        self.assertNotIn(self.inline.A, self.enum)
        self.assertNotIn(self.enum.A, self.inline)
        
    def test_subclass(self):
        self.assertTrue(issubclass(self.inline, Enum))
        self.assertTrue(issubclass(self.enum, Enum))

    def test_equal(self):
        self.assertEqual(self.inline.A.value, 0)
        self.assertEqual(self.enum.A.value, 0)
        self.assertNotEqual(self.enum.A, self.inline.A)
        self.assertEqual(self.enum.A.value, self.inline.A.value)
        self.assertNotEqual(self.enum.A, self.enum.B)
        
    def test_add(self):
        self.assertEqual(self.enum.A + 3, 3)
        self.assertEqual(self.enum.A + 5, self.enum.D)
        self.assertEqual(self.enum.A + self.inline.B, 1)
        
    def test_sub(self):
        self.assertEqual(self.enum.D - 2, 3)
        self.assertEqual(self.enum.D - self.enum.C, 3)
        self.assertEqual(self.enum.D - self.inline.C, 3)
        
    def test_mul(self):
        self.assertEqual(self.enum.D * 2, 10)
        self.assertEqual(self.enum.D * self.enum.C, 10)
        self.assertEqual(self.enum.D * self.inline.C, 10)
        
    def test_div(self):
        self.assertEqual(self.enum.C / 2, 1)
        self.assertEqual(self.enum.C / self.enum.C, 1)
        self.assertEqual(self.enum.C / self.inline.C, 1)
        
    def test_floordiv(self):
        self.assertEqual(self.enum.D / 2, 2)
        self.assertEqual(self.enum.D / self.enum.C, 2)
        self.assertEqual(self.enum.D / self.inline.C, 2)
        
    def test_mod(self):
        self.assertEqual(self.enum.D % 2, 1)
        self.assertEqual(self.enum.D % self.enum.C, 1)
        self.assertEqual(self.enum.D % self.inline.C, 1)
        
    def test_divmod(self):
        x = divmod(self.enum.D, 2)
        self.assertEqual(x[0], 2)
        self.assertEqual(x[1], 1)
        
        x = divmod(self.enum.D, self.enum.C)
        self.assertEqual(x[0], 2)
        self.assertEqual(x[1], 1)
        
        x = divmod(self.enum.D, self.inline.C)
        self.assertEqual(x[0], 2)
        self.assertEqual(x[1], 1)
        
    def test_pow(self):
        self.assertEqual(self.enum.D ** 2, 25)
        self.assertEqual(self.enum.D ** self.enum.C, 25)
        self.assertEqual(self.enum.D ** self.inline.C, 25)
        
        self.assertEqual(pow(self.enum.D , 2), 25)
        self.assertEqual(pow(self.enum.D , self.enum.C), 25)
        self.assertEqual(pow(self.enum.D , self.inline.C), 25)
        
    def test_lshift(self):
        self.assertEqual(self.enum.D << 2, 20)
        self.assertEqual(self.enum.D << self.enum.C, 20)
        self.assertEqual(self.enum.D << self.inline.C, 20)
        
    def test_rshift(self):
        self.assertEqual(self.enum.D >> 1, 2)
        self.assertEqual(self.enum.D >> self.enum.B, 2)
        self.assertEqual(self.enum.D >> self.inline.B, 2)
        
    def test_and(self):
        self.assertEqual(self.enum.D & 2, 0)
        self.assertEqual(self.enum.D & self.enum.C, 0)
        self.assertEqual(self.enum.D & self.inline.C, 0)
        
    def test_or(self):
        self.assertEqual(self.enum.D | 2, 7)
        self.assertEqual(self.enum.D | self.enum.C, 7)
        self.assertEqual(self.enum.D | self.inline.C, 7)
        
    def test_xor(self):
        self.assertEqual(self.enum.D ^ 1, 4)
        self.assertEqual(self.enum.D ^ self.enum.B, 4)
        self.assertEqual(self.enum.D ^ self.inline.B, 4)