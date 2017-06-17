#!/usr/bin/env python

# Copyright (c) 2017 Matt Struble. All Rights Reserved.
#
# Use is subject to license terms.
#
# Author: Matt Struble
# Date: Jun. 16 2017
from event import Event
from enum import Enum

class MouseButton(Enum):
    LEFT = "LEFT"
    MIDDLE = "MIDDLE"
    RIGHT = "RIGHT"


class MouseButtonEvent(Event):

    DOWN = "MOUSE_DOWN"
    UP = "MOUSE_UP"

    def __init__(self, etype, button, time=None):
        super(MouseButtonEvent, self).__init__(etype, time)

        self.button = button

    def __repr__(self):
        return 'MouseButtonEvent({} {} {})'.format(self.etype, self.button, self.time)

class MouseWheelEvent(Event):

    WHEEL = "MOUSE_WHEEL"

    def __init__(self, etype, delta, time=None):
        super(MouseWheelEvent, self).__init__(etype, time)

        self.delta = delta

    def __repr__(self):
        return "MouseWheelEvent({} {} {})".format(self.etype, self.delta, self.time)

class MouseMoveEvent(Event):

    MOVE = "MOUSE_MOVE"

    def __init__(self, etype, x, y, time=None):
        super(MouseWheelEvent, self).__init__(etype, time)

        self.x = x
        self.y = y

    def __repr__(self):
        return "MouseMoveEvent({} ({},{}) {})".format(self.etype, self.x, self.y, self.time)
