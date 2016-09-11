#! /usr/bin/env python

""" Handles system level events. Static class. """

# Author: Matt Struble
# Date: Sep. 11 2016
#---------------------------------------------------------------------

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
        if event in EventHandler._eListeners:
            EventHandler._eListeners[event].append(func)
        else:
            EventHandler._eListeners[event] = [func]



