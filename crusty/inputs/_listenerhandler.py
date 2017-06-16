#!/usr/bin/env python

# Copyright (c) 2017 Matt Struble. All Rights Reserved. 
#
# Use is subject to license terms.
#
# Author: Matt Struble
# Date: Jun. 15 2017
from _keyboardlistener import KeyboardListener as __KeyboardListener
from eventhandler import EventHandler

__kbListener = __KeyboardListener()

__kbListener.addHandler(EventHandler.eventHandler)
__kbListener.start()

