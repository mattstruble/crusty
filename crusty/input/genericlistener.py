#! /usr/bin/env python

""" Handles Keyboard events. """

# Author: Matt Struble
# Date: Sep. 11 2016
# Code adapted from: https://github.com/boppreh/keyboard/
#---------------------------------------------------------------------
from threading import Thread
import traceback
import functools

class GenericListener(object):
    def __init__(self):
        self.handlers = []
        self.listening = False

    def invokeHandlers(self, event):
        for handler in self.handlers:
            try:
                handler(event)
            except Exception as e:
                traceback.print_exc()

    def start(self):
        if not self.listening:
            self.listening = True
            self.listening_thread = Thread(target=self.listen)
            self.listening_thread.daemon = True
            self.listening_thread.start()

    def wrap(self, func):
        """ Wraps function ensuring listener thread is active. """
        @functools.wraps(func)
        def wrapper(*args, **kwds):
            if not self.listening:
                self.listening = True
                self.listening_thread = Thread(target=self.listen)
                self.listening_thread.daemon = True
                self.listening_thread.start()
            return func(*args, **kwds)
        return wrapper

    def addHandler(self, handler):
        """ Adds function to receive captured events. """
        self.handlers.append(handler)

    def removeHandler(self, handler):
        """ Removes a previously added event handler. """
        self.handlers.remove(handler)
