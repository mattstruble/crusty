#!/usr/bin/env python

# Copyright (c) 2017 Matt Struble. All Rights Reserved. 
#
# Use is subject to license terms.
#
# Author: Matt Struble
# Date: Jun. 11 2017
from datetime import datetime

class Event(object):
    
    def __init__(self, time=None):
        self.time = datetime.now() if time is None else time