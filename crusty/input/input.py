#! /usr/bin/env python

""" Processes user input. Static class. """

# Author: Matt Struble
# Date: Sep. 10 2016
#---------------------------------------------------------------------

class Input:

    _active = False
    _waitState = []
    _keyState = []
    _oldState = []

    _lastKey = -1

    _groups = {}

    _keyboardString = ""
    _keyboardStringMaxLength = 255

    keyboardEnabled = True
    repeatTimeInitial = -1
    repeatTimeRepeat = -1
    
    @classmethod
    def getKeyboardString():
        """ Returns string composed of keyboard presses. """
        return _keyboardString

    @classmethod
    def setKeyboardString(string):
        """ Sets string composed of keyboard presses. """
        if not isinstance(string, basestring):
            raise TypeError("KeyboardString must be a string.")

        _keyboardString = string

    @classmethod
    def getKeyboardStringMaxLength():
        """ Returns the max keyboard string length. """
        return _keyboardStringMaxLength

    @classmethod
    def setKeyboardStringMaxLength(length):
        """ Sets max keyboard string length. """
        if not isinstance(length, int):
            raise TypeError("KeyboardStringMaxLength must be an int.")

        _keyboardStringMaxLength = length
        if( len(_keyboardString) > _keyboardStringMaxLength ):
            _keyboardString = _keyboardString[:(len(_keyboardString) - _keyboardStringMaxLength)]

    @classmethod
    def setGroup(name, *keys):
        """ Groups the given inputs under the given name. """
        if not isinstance(name, basestring):
            raise TypeError("Group name needs to be a string.")

        if not all(isinstance(x, int) for x in keys):
            raise TypeError("Keys must be int.")

        _groups[name] = list(keys)

    @classmethod
    def getGroup(name):
        """ Returns a list of keys in the given group. """
        if not isinstance(name, basestring):
             raise TypeError("Group name needs to be a string.")

        return _groups[name]
    
    @classmethod
    def clearGroup(name):
        """ Clears the group of inputs with the given name."""
        if not isinistance(name, basestring):
            raise TypeError("Group name needs to be a string.")

        del _groups[name]

    @classmethod
    def clearGroups(*names):
        """ Clears the groups with the given names. """
        if not all(isinstance(x, basestring) for x in names):
            raise TypeError("Group name needs to be a string.")

        for name in names:
            clearGroup(name)

    @classmethod
    def clearAllGroups():
        """ Clears all grouped input. """
        _groups.clear()

    @classmethod
    def check(key = -1):
        """ Checks if the given input is down. -1 for any key. """
        if not isinstance(key, int):
            raise TypeError("Key needs to be an int.")

        if not -1 <= key < 256:
            raise IndexError("Key needs to be between -1 and 256")

        if( key == -1 ):
            for i in range(0, 256):
                if keyAllowed(i) and _keyState[i] == True:
                    return True
            return False

        return keyAllowed(key) and _keyState[key] == True
        
    @classmethod
    def checkGroup(name):
        """ Returns if the given input group is pressed. """
        if not isinstance(name, basestring):
            raise TypeError("Group name needs to be a string.")

        for key in _groups[name]:
            if check(key):
                return True
            
        return False

    @classmethod
    def pressed(key = -1):
        """ Returns if the given input is pressed. -1 for any key. """
        if not isinstance(key, int):
            raise TypeError("Key needs to be an int.")

        if not -1 <= key < 256:
            raise IndexError("Key needs to be between -1 and 256")
        
        if key == -1:
            for i in range(0, 256):
                if( keyAllowed(i) and _keyState[i] == True and _oldState[i] == False):
                    return True
            return False

        return ( keyAllowed(key) and _keyState[key] == True and _oldState[key] == False)

    @classmethod
    def pressedGroup(name):
        """ Returns if the given input group is pressed. """
        if not isinstance(name, basestring):
            raise TypeError("Group name needs to be a string.")

        for key in _groups[name]:
            if pressed(key):
                return True

        return False

    @classmethod
    def pressedRepeat(key = -1):
        """ Returns if the given input is pressed, allowing for repeats. -1 for any key. """
        if not isinstance(key, int):
            raise TypeError("Key needs to be an int.")

        if not -1 <= key < 256:
            raise IndexError("Key needs to be between -1 and 256")

        if key == -1:
            for i in range(0, 256):
                if ( keyAllowed(i) and ( ( _keyState[i] == True and _oldState[i] == False) or _waitState[i] == 0) ):
                    return True
                return False

        return ( keyAllowed(i) and ( ( _keyState[key] == True and _oldState[key] == False) or _waitState[key] == 0) )

    @classmethod
    def pressedRepeatGroup(name):
        """ Returns if the given input group is pressed, allowing for repeats. """
        if not isinstance(name, basestring):
            raise TypeError("Group name needs to be a string.")

        for key in _groups[name]:
            if pressedRepeat(key):
                return True

        return False
            
    @classmethod
    def released(key = -1):
        """ Returns if the given input is released. -1 for any key."""
        if not isinstance(key, int):
            raise TypeError("Key needs to be an int.")

        if not -1 <= key < 256:
            raise IndexError("Key needs to be between -1 and 256")

        if key == -1:
            for i in range(0, 256):
                if keyAllowed(i) and _keyState[i] == False and _oldState[i] == True:
                    return True
            return False

        return keyAllowed(key) and _keyState[key] == False and _oldState[key] == True

    @classmethod
    def releasedGroup(name):
        if not isinstance(name, basestring):
            raise TypeError("Group name needs to be a string.")

        for key in _groups[name]:
            if released(key):
                return True

        return False

    @classmethod
    def clearInput():
        """ Clears all input. """
        for i in range(0, 256):
            _oldState[i] = _keyState[i] = False
            _waitState[i] = -1

    def activate():
        if not _activate:
            repeatTimeInitial = 32
            repeatTimeRepeat = 10
            _activate = True

    
