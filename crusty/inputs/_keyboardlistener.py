#!/usr/bin/env python

# Copyright (c) 2017 Matt Struble. All Rights Reserved. 
#
# Use is subject to license terms.
#
# Author: Matt Struble
# Date: Jun. 11 2017
import platform
from _genericlistener import GenericListener
from keyboardevent import KeyboardEvent

if platform.system() == 'Windows':
    import _winkeyboard as keyboard

class KeyboardListener(GenericListener):
    def callback(self, event):
        if not event.scan:
            return

        return self.invokeHandlers(event)

    def listen(self):
        keyboard.listen(self.callback)