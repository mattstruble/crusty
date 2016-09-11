#! /usr/bin/env python

""" Handles Keyboard events. """

# Author: Matt Struble
# Date: Sep. 11 2016
#---------------------------------------------------------------------
from time import time as now

class KeyboardEvent(object):

    KEY_DOWN = 0
    KEY_UP = 1
    
    def __init__(self, etype, keycode, scancode, is_alt=False, time=None):
        self.etype = etype
        self.key = keycode
        self.scan = scancode
        self.alt = is_alt
        self.time = now() if time is None else time
