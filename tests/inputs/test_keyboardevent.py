#!/usr/bin/env python

# Copyright (c) 2017 Matt Struble. All Rights Reserved.
#
# Use is subject to license terms.
#
# Author: Matt Struble
# Date: Jun. 16 2017
from datetime import datetime
from unittest import TestCase
from crusty.inputs import KeyboardEvent, Keys

class TestKeyboardEventCase(TestCase):

    def test_creation(self):
        time = datetime.now()
        kbe = KeyboardEvent(KeyboardEvent.KEY_DOWN, Keys.A, Keys.A, 0)
        self.assertTrue(abs(kbe.time - time).microseconds < 100)

        self.assertEqual(KeyboardEvent.KEY_DOWN, kbe.etype)
        self.assertEqual(Keys.A, kbe.key)

        kbe = KeyboardEvent(KeyboardEvent.KEY_DOWN, Keys.A, Keys.A, 0, False, time)
        self.assertEqual(kbe.time, time)
