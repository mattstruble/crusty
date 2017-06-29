#!/usr/bin/env python

# Copyright (c) 2017 Matt Struble. All Rights Reserved.
#
# Use is subject to license terms.
#
# Author: Matt Struble
# Date: Jun. 15 2017
from unittest import TestCase
from crusty.inputs import Keyboard, Keys, KeyboardEvent

class KeyboardTestCase(TestCase):

    def resetKeyboard(self):
        self.keyboard.clearInput()
        self.keyboard.setKeyboardString()

    def setUp(self):
        self.keyboard = Keyboard
        self.keyboard.initialize()

    def tearDown(self):
        self.keyboard.terminate()

    def keyDown(self, key):
        event = KeyboardEvent(KeyboardEvent.KEY_DOWN, key.value, key.value, 0)
        self.keyboard._onKeyDown(event)

    def keyUp(self, key):
        event = KeyboardEvent(KeyboardEvent.KEY_UP, key.value, key.value, 0)
        self.keyboard._onKeyUp(event)

    def test_init(self):
        self.resetKeyboard()

        for state in self.keyboard._keyState:
            self.assertFalse(state)

        for state in self.keyboard._oldState:
            self.assertFalse(state)

        for state in self.keyboard._waitState:
            self.assertEqual(state, -1)

        self.assertTrue(self.keyboard.Enabled)

    def test_down(self):
        self.resetKeyboard()

        self.assertFalse(self.keyboard.down(Keys.A))
        self.keyDown(Keys.A)
        self.assertTrue(self.keyboard.down(Keys.A))
        self.assertTrue(self.keyboard.down())

        self.assertRaises(TypeError, self.keyboard.down, 7)

    def test_press(self):
        self.resetKeyboard()

        self.keyDown(Keys.A)
        self.assertTrue(self.keyboard.pressed(Keys.A))
        self.assertTrue(self.keyboard.pressed())
        self.keyboard._update()
        self.keyDown(Keys.A)
        self.assertFalse(self.keyboard.pressed(Keys.A))
        self.assertFalse(self.keyboard.pressed())

        self.assertRaises(TypeError, self.keyboard.pressed, 7)

    def test_release(self):
        self.resetKeyboard()

        self.keyDown(Keys.A)
        self.assertFalse(self.keyboard.released(Keys.A))
        self.assertFalse(self.keyboard.released())
        self.keyboard._update()
        self.keyUp(Keys.A)
        self.assertTrue(self.keyboard.released(Keys.A))
        self.assertTrue(self.keyboard.released())

        self.assertRaises(TypeError, self.keyboard.released, 7)

    def test_keyboardString(self):
        self.resetKeyboard()
        self.assertEqual(self.keyboard.getKeyboardString(), "")

        self.keyDown(Keys.T)
        self.keyDown(Keys.E)
        self.keyDown(Keys.S)
        self.keyDown(Keys.T)

        self.assertEqual(self.keyboard.getKeyboardString(), "TEST")

        self.assertRaises(TypeError, self.keyboard.setKeyboardString, 7)

    def test_maxKeyboardStringLength(self):
        self.resetKeyboard()
        self.assertEqual(self.keyboard.getKeyboardStringMaxLength(), self.keyboard._stringMaxLength)

        self.keyboard.setKeyboardStringMaxLength(5)
        self.assertEqual(self.keyboard.getKeyboardStringMaxLength(), 5)
        for i in range(65, 71):
            self.keyDown(Keys.getKey(i))

        self.assertEqual(self.keyboard.getKeyboardString(), "BCDEF")

        self.assertRaises(TypeError, self.keyboard.setKeyboardStringMaxLength, "fail")
