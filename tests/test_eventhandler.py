#!/usr/bin/env python

# Copyright (c) 2017 Matt Struble. All Rights Reserved.
#
# Use is subject to license terms.
#
# Author: Matt Struble
# Date: Jun. 16 2017
from unittest import TestCase
from mock import Mock
from crusty import EventHandler, Event

class EventHandlerTestCase(TestCase):

    def setUp(self):
        self.handler = EventHandler

    def callback(self, event):
        pass

    def tearDown(self):
        self.handler.removeAllListeners()

    def test_add(self):
        self.assertEqual(len(self.handler._eListeners), 0)
        self.handler.addEventListener(Event.DEFAULT, self.callback)
        self.assertEqual(len(self.handler._eListeners), 1)
        self.assertTrue(self.callback in self.handler._eListeners[Event.DEFAULT])
        self.handler.addEventListener(Event.DEFAULT, self.callback)
        self.assertEqual(len(self.handler._eListeners), 1)
        self.handler.addEventListener("TestEvent", self.callback)
        self.assertEqual(len(self.handler._eListeners), 2)

    def test_call(self):
        event = Event("TestCall")
        f = Mock()
        self.handler.addEventListener(event.etype, f)
        self.handler.eventHandler(event)
        f.assert_called_with(event)

    def test_remove(self):
        event = Event("TestRemove")
        self.handler.addEventListener(event.etype, self.callback)
        self.assertTrue(self.callback in self.handler._eListeners[event.etype])
        self.handler.removeEventListener(event.etype, self.callback)
        self.assertFalse(event.etype in self.handler._eListeners)

        self.handler.removeAllListeners()
        self.assertEqual(len(self.handler._eListeners), 0)
