#! /usr/bin/env python

""" Handles terminal input. Static class. """

# Author: Matt Struble
# Date: Sep. 10 2016
# depricated see eventhandler
#---------------------------------------------------------------------
from msvcrt import getch

class KeyboardEvent:
    KEY_DOWN = 0
    KEY_UP = 1

class InputHandler:

    _previousInput = -1

    _listeners = {}

    @staticmethod
    def update():
        InputHandler._handleKeyboard()

    @staticmethod
    def addInputListener(event, func):
        """ Adds function call to event handler

            Parameters
            ----------
            event : int
                Integer representation of event type.
            func : function()
                Callable function for event triggers.
        """
        if not isinstance(event, int):
            raise TypeError("You must pass in a valid event type.")

        if not callable(func):
            raise TypeError("You must pass in a valid function.")

        if event > -1:
            if event in InputHandler._listeners:
                InputHandler._listeners[event].append(func)
            else:
                InputHandler._listeners[event] = [func]
            

    @staticmethod
    def _handleKeyboard():
        key = ord(getch())
        prev = InputHandler._previousInput
        listeners = InputHandler._listeners

        if key is not prev:

            if KeyboardEvent.KEY_DOWN in listeners:
                for keyDown in listeners[KeyboardEvent.KEY_DOWN]:
                    keyDown(key)
                    
            if KeyboardEvent.KEY_UP in listeners:
                for keyUp in listeners[KeyboardEvent.KEY_UP]:
                    keyUp(prev)

        InputHandler._previousInput = key
