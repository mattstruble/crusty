#!/usr/bin/env python

# Copyright (c) 2016 Matt Struble. All Rights Reserved. 
#
# Use is subject to license terms.
#
# Author: Matt Struble
# Date: Sep. 11 2016
import time, platform
from keyboardevent import KeyboardEvent
from genericlistener import GenericListener

if platform.system() == 'Windows':
    import winkeyboard as oskeyboard

class KeyboardListener(GenericListener):
    def callback(self, event):
        if not event.scan:
            return

        return self.invokeHandlers(event)

    def listen(self):
        oskeyboard.listen(self.callback)

kbListener = KeyboardListener()

class EventHandler(object):
    """ Handles system level events. Static class. """
    
    _eListeners = {}

    @staticmethod
    def initialize():
        kbListener.addHandler(EventHandler.eventHandler)
        kbListener.start()

    @staticmethod
    def eventHandler(event):
        if event.etype in EventHandler._eListeners:
            for listener in EventHandler._eListeners[event.etype]:
                listener(event)

    @staticmethod
    def addEventListener(event, func):
        
        if not isinstance(event, Event):
            raise TypeError("event must be a valid Event")
        
        if not callable(func):
            raise TypeError("func must be a callable type")
        
        if event in EventHandler._eListeners:
            EventHandler._eListeners[event].append(func)
        else:
            EventHandler._eListeners[event] = [func]
            
    @staticmethod
    def removeEventListener(event, func):
        
        if not isinstance(event, Event):
            raise TypeError("event must be a valid Event")
        
        if not callable(func):
            raise TypeError("func must be a callable type")
        
        if event in EventHandler._eListeners:
            if func in EventHandler._eListeners[event]:
                EventHandler._eListeners[event].remove(func)
            
            if len(EventHandler._eListeners[event] == 0):
                EventHandler._eListeners.remove(event)



