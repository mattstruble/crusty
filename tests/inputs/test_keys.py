#!/usr/bin/env python

# Copyright (c) 2017 Matt Struble. All Rights Reserved. 
#
# Use is subject to license terms.
#
# Author: Matt Struble
# Date: Jun. 15 2017
from unittest import TestCase
from crusty.inputs import Keys

class KeysTestCase(TestCase):
    
    def test_getKey(self):
        for key in Keys:
            tKey = Keys.getKey(key.value)
            self.assertTrue(tKey == key)
            
        self.assertIsNone(Keys.getKey(300))