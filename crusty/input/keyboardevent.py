#!/usr/bin/env python

# Copyright (c) 2016 Matt Struble. All Rights Reserved. 
#
# Use is subject to license terms.
# 
# Author: Matt Struble
# Date: Sep. 11 2016
from crusty.event import Event

class KeyboardEvent(Event):

    KEY_DOWN = "KEY_DOWN"
    KEY_UP = "KEY_UP"
    
    def __init__(self, etype, key, keycode, scancode, is_alt=False, time=None):
		super(KeyboardEvent, self).__init__(etype, time)
        
		self.key = key
        self.keycode = keycode
        self.scan = scancode
        self.alt = is_alt
        
	def __repr__(self):
		return 'KeyboardEvent({} {} {})'.format(self.etype, self.key, self.time)
