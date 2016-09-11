#! /usr/bin/env python

""" Processes user input. Static class. """

# Author: Matt Struble
# Date: Sep. 10 2016
#---------------------------------------------------------------------

from keys import Keys
from inputhandler import *

class Input:

    _active = False
    _waitState = [-1] * 256
    _keyState = [False] * 256
    _oldState = [False] * 256

    _lastKey = -1

    _groups = {}

    _keyboardString = ""
    _keyboardStringMaxLength = 255

    keyboardEnabled = True
    repeatTimeInitial = -1
    repeatTimeRepeat = -1
    
    @staticmethod
    def getKeyboardString():
        """ Returns string composed of keyboard presses. """
        return Input._keyboardString

    @staticmethod
    def setKeyboardString(string):
        """ Sets string composed of keyboard presses. """
        if not isinstance(string, basestring):
            raise TypeError("KeyboardString must be a string.")

        Input._keyboardString = string

    @staticmethod
    def getKeyboardStringMaxLength():
        """ Returns the max keyboard string length. """
        return Input._keyboardStringMaxLength

    @staticmethod
    def setKeyboardStringMaxLength(length):
        """ Sets max keyboard string length. """
        if not isinstance(length, int):
            raise TypeError("KeyboardStringMaxLength must be an int.")

        Input._keyboardStringMaxLength = length
        if( len(Input._keyboardString) > Input._keyboardStringMaxLength ):
           Input._keyboardString = Input._keyboardString[:(len(Input._keyboardString) - Input._keyboardStringMaxLength)]

    @staticmethod
    def setGroup(name, *keys):
        """ Groups the given inputs under the given name. """
        if not isinstance(name, basestring):
            raise TypeError("Group name needs to be a string.")

        if not all(isinstance(x, int) for x in keys):
            raise TypeError("Keys must be int.")

        Input._groups[name] = list(keys)

    @staticmethod
    def getGroup(name):
        """ Returns a list of keys in the given group. """
        if not isinstance(name, basestring):
             raise TypeError("Group name needs to be a string.")

        return Input._groups[name]
    
    @staticmethod
    def clearGroup(name):
        """ Clears the group of inputs with the given name."""
        if not isinistance(name, basestring):
            raise TypeError("Group name needs to be a string.")

        del Input._groups[name]

    @staticmethod
    def clearGroups(*names):
        """ Clears the groups with the given names. """
        if not all(isinstance(x, basestring) for x in names):
            raise TypeError("Group name needs to be a string.")

        for name in names:
            clearGroup(name)

    @staticmethod
    def clearAllGroups():
        """ Clears all grouped input. """
        Input._groups.clear()

    @staticmethod
    def down(key = -1):
        """ Returns if the given input is down. -1 for any key. """
        if not isinstance(key, int):
            raise TypeError("Key needs to be an int.")

        if not -1 <= key < 256:
            raise IndexError("Key needs to be between -1 and 256")

        if( key == -1 ):
            for i in range(0, 256):
                if Input._keyAllowed(i) and Input._keyState[i] == True:
                    return True
            return False

        return Input._keyAllowed(key) and Input._keyState[key] == True
        
    @staticmethod
    def downGroup(name):
        """ Returns if the given input group is down. """
        if not isinstance(name, basestring):
            raise TypeError("Group name needs to be a string.")

        for key in Input._groups[name]:
            if down(key):
                return True
            
        return False

    @staticmethod
    def pressed(key = -1):
        """ Returns if the given input is pressed. -1 for any key. """
        if not isinstance(key, int):
            raise TypeError("Key needs to be an int.")

        if not -1 <= key < 256:
            raise IndexError("Key needs to be between -1 and 256")
        
        if key == -1:
            for i in range(0, 256):
                if( Input._keyAllowed(i) and Input._keyState[i] == True and Input._oldState[i] == False):
                    return True
            return False

        return ( Input._keyAllowed(key) and Input._keyState[key] == True and Input._oldState[key] == False)

    @staticmethod
    def pressedGroup(name):
        """ Returns if the given input group is pressed. """
        if not isinstance(name, basestring):
            raise TypeError("Group name needs to be a string.")

        for key in Input._groups[name]:
            if pressed(key):
                return True

        return False

    @staticmethod
    def pressedRepeat(key = -1):
        """ Returns if the given input is pressed, allowing for repeats. -1 for any key. """
        if not isinstance(key, int):
            raise TypeError("Key needs to be an int.")

        if not -1 <= key < 256:
            raise IndexError("Key needs to be between -1 and 256")

        if key == -1:
            for i in range(0, 256):
                if ( Input._keyAllowed(i) and ( ( Input._keyState[i] == True and Input._oldState[i] == False) or Input._waitState[i] == 0) ):
                    return True
                return False

        return ( Input._keyAllowed(i) and ( ( Input._keyState[key] == True and Input._oldState[key] == False) or Input._waitState[key] == 0) )

    @staticmethod
    def pressedRepeatGroup(name):
        """ Returns if the given input group is pressed, allowing for repeats. """
        if not isinstance(name, basestring):
            raise TypeError("Group name needs to be a string.")

        for key in Input._groups[name]:
            if pressedRepeat(key):
                return True

        return False
            
    @staticmethod
    def released(key = -1):
        """ Returns if the given input is released. -1 for any key."""
        if not isinstance(key, int):
            raise TypeError("Key needs to be an int.")

        if not -1 <= key < 256:
            raise IndexError("Key needs to be between -1 and 256")

        if key == -1:
            for i in range(0, 256):
                if Input._keyAllowed(i) and Input._keyState[i] == False and Input._oldState[i] == True:
                    return True
            return False

        return Input._keyAllowed(key) and Input._keyState[key] == False and Input._oldState[key] == True

    @staticmethod
    def releasedGroup(name):
        """ Returns if the given input group is released. """
        if not isinstance(name, basestring):
            raise TypeError("Group name needs to be a string.")

        for key in Input._groups[name]:
            if released(key):
                return True

        return False

    @staticmethod
    def clearInput():
        """ Clears all input. """
        for i in range(0, 256):
            Input._oldState[i] = Input._keyState[i] = False
            Input._waitState[i] = -1

    @staticmethod
    def activate():
        """ Activates the input manager. """
        if not Input._active:
            Input.repeatTimeInitial = 32
            Input.repeatTimeRepeat = 10

            InputHandler.addInputListener(KeyboardEvent.KEY_DOWN, Input._onKeyDown)
            InputHandler.addInputListener(KeyboardEvent.KEY_UP, Input._onKeyUp)
            
            Input._active = True

    @staticmethod
    def _update():
        for i in range(0, 256):
            Input._oldState[i] = Input._keyState[i]
            if Input._keyState[i] == True:
                if Input._waitState[i] == -1:
                    Input._waitState[i] = Input.repeatTimeInitial
                elif Input._waitState[i] == 0:
                    Input._waitState[i] = Input.repeatTimeRepeat
                else:
                    Input._waitState[i] -= 1
            else:
                Input._waitState[i] = -1

    @staticmethod
    def _onKeyDown(keyCode):
        if not isinstance(keyCode, int):
            TypeError("Keycode needs to be an int")

        if not 0 < keyCode < 256:
            return

        Input._lastKey = keyCode
        Input._keyState[keyCode] = True

        if keyCode == Keys.BACK:
            Input._keyboardString = Input._keyboardString[:-1]
        elif keyCode > 31 and keyCode is not 127:
            Input._keyboardString += chr(keyCode)
            if len(Input._keyboardString) > Input._keyboardStringMaxLength:
                Input._keyboardString = Input._keyboardString[1:]

    @staticmethod
    def _onKeyUp(keyCode):
        if not isinstance(keyCode, int):
            TypeError("Keycode needs to be an int")

        if not 0 < keyCode < 256:
            return

        Input._lastKey = keyCode
        Input._keyState[keyCode] = False

    @staticmethod
    def _keyAllowed(key):
        if Input.keyboardEnabled:
            return True
        return False
