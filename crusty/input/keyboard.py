#!/usr/bin/env python

# Copyright (c) 2016 Matt Struble. All Rights Reserved. 
#
# Use is subject to license terms.
# 
# Author: Matt Struble
# Date: Sep. 11 2016
from keyboardevent import KeyboardEvent
from keys import Keys
from eventhandler import EventHandler

class Keyboard(object):

    Enabled = False

    _string = ""
    _stringMaxLength = 255

    _waitState = [-1] * 256
    _keyState = [False] * 256
    _oldState = [False] * 256

    _lastKey = -1
    _repeatTimeInitial = -1
    _repeatTimeRepeat = -1
    
    @staticmethod
    def activate():
        if not Keyboard.Enabled:
            Keyboard._repeatTimeInitial = 32
            Keybaord._repeatTimeRepeat = 10
            
            EventHandler.addEventListener(KeyboardEvent.KEY_DOWN, Keyboard._onKeyDown)
            EventHandler.addEventListener(KeyBoardEvent.KEY_UP, Keyboard._onKeyUp)
            
    @staticmethod
    def deactivate():
        if Keyboard.Enabled:
            Keyboard._repeatTimeInitial = -1
            Keybaord._repeatTimeRepeat = -1
            
            EventHandler.removeEventListener(KeyboardEvent.KEY_DOWN, Keyboard._onKeyDown)
            EventHandler.removeEventListener(KeyBoardEvent.KEY_UP, Keyboard._onKeyUp)        

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
        
        if len(string) > Keyboard._stringMaxLength:
            raise RuntimeError("string exceeds the bounds of keyboard string max length")
        
        Keyboard._string = string
        
    @staticmethod
    def getKeyboardStringMaxLength():
        return Keyboard._stringMaxLength
    
    
    @staticmethod
    def setKeyboardStringMaxLength(length):
        """ Sets max keyboard string length.

            Parameters
            ----------
            length : int
                Maximum length allowable for keyboard sring
        """
        if not isinstance(length, int):
            raise TypeError("KeyboardStringMaxLength must be an int.")

        Keyboard._stringMaxLength = length
        if( len(Keyboard._string) > Keyboard._stringMaxLength ):
           Keyboard._string = Keyboard._string[:(len(Keyboard._string) - Keyboard._stringMaxLength)]
           
    @staticmethod
    def down(key = Keys.ANY):
        if not key in Keys:
            raise TypeError("key needs to be a Key")
        
        if key == Keys.ANY:
            for i in range(0, 256):
                if Keyboard._keyAllowed(i) and Keyboard._keyState[i] == True:
                    return True
            return False
        
        return Keyboard._keyAllowed(key) and Keyboard._keyState[key.value]
    
    @staticmethod
    def pressed(key = Keys.ANY):
        if key != Keys:
            raise TypeError("key needs to be a Key")
        
        if key == Keys.ANY:
            for i in range(0, 256):
                if( Keyboard._keyAllowed(i) and Keyboard._keyState[i] == True and Keyboard._oldState[i] == False):
                    return True
            return False
    
        return ( Keyboard._keyAllowed(key) and Keyboard._keyState[key.value] == True and Keyboard._oldState[key.value] == False)
    
    @staticmethod
    def released(key = Keys.ANY):
        if key != Keys:
            raise TypeError("key needs to be a Key")

        if key == -1:
            for i in range(0, 256):
                if Keyboard._keyAllowed(i) and Keyboard._keyState[i] == False and Keyboard._oldState[i] == True:
                    return True
            return False

        return Keyboard._keyAllowed(key) and Keyboard._keyState[key.value] == False and Keyboard._oldState[key.value] == True
    
    @staticmethod
    def clearInput():
        for i in range(0, 256):
            Keyboard._oldState[i] = Keyboard._keyState[i] = False
            Keyboard._waitState[i] = -1
    
    
    @staticmethod
    def _keyAllowed(Key):
        if key != Keys:
            raise TypeError("key needs to be a Key")
        
        return Keyboard.Enabled
    
    @staticmethod
    def _onKeyDown(event):
        if isinstance(event, KeyboardEvent):
            Keyboard._lastKey = event.key
            Keyboard._keyState[event.key] = True
            
            if event.key == Keys.BACK and len(Keyboard._string) > 0:
                Keyboard._string = Keyboard._string[:-1]
            elif event.key > 31 and event.key is not 127:
                Keyboard._string += chr(event.key)
                if len(Keyboard._string) > Keyboard._stringMaxLength:
                    Keyboard._string = Keyboard._string[1:]
                    
    @staticmethod
    def _onKeyUp(event):
        if isinstance(event, KeyboardEvent):
            Keyboard._lastKey = event.key
            Keyboard._keyState[event.key] = False

    """
        TODO:
            Grouping?
            Child of Input to allow multi-input grouping? 

    """

    
