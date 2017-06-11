#!/usr/bin/env python

# Copyright (c) 2016 Matt Struble. All Rights Reserved. 
#
# Use is subject to license terms.
# 
# Author: Matt Struble
# Date: Sep. 11 2016
from keyboardevent import KeyboardEvent
from keys import Keys

class Keyboard(object):

    Enabled = False

    _string = ""
    _stringMaxLength = 255

    _waitState = [-1] * 256
    _keyState = [False] * 256
    _oldState = [False] * 256

    _lastKey = -1

    @staticmethod
    def getKeyboardString():
        """ Returns string composed of recent keyboard presses. """
        return Keyboard._string

    @staticmethod
    def setKeyboardString(string):
        """ Sets string composed of recent keyboard presses.

            Parameters
            ----------
            string : String
                String to replace keyboard string with.
        """
        if not isinstance(string, basestring):
            raise TypeError("Keyboard string must be a string.")

        Keyboard._string = string

    """
        TODO

        Need to set up as main listener to eventhandler for keyboard events.

        Need to set up up / down / released logic

        make child of Input? So that will allow grouping of various inputs?

        """

    
