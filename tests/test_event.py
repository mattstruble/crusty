#!/usr/bin/env python

# Copyright (c) 2017 Matt Struble. All Rights Reserved.
#
# Use is subject to license terms.
#
# Author: Matt Struble
# Date: Jun. 16 2017
from datetime import datetime
from unittest import TestCase
from crusty import Event

class EventTestCase(TestCase):

    def test_init(self):
        time = datetime.now()
        ev = Event()
        self.assertTrue(abs(ev.time - time).microseconds < 100)
        self.assertEqual(Event.DEFAULT, ev.etype)

        ev = Event(Event.DEFAULT, time)
        self.assertEqual(ev.time, time)
