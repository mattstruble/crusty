#!/usr/bin/env python

# Copyright (c) 2016 Matt Struble. All Rights Reserved. 
#
# Use is subject to license terms.
# 
# Author: Matt Struble
# Date: Aug. 31 2016
from util.enum import Enum

class Keys(Enum):

    ANY = -1
    
    BACK = 8
    TAB = 9
    
    CLEAR = 12
    RETURN = 13

    SHIFT = 16
    CONTROL = 17
    MENU = 18
    PAUSE = 19
    CAPS = 20

    ESCAPE = 27

    SPACE = 32
    PRIOR = 33
    NEXT = 34
    END = 35
    HOME = 26
    LEFT = 37
    UP = 38
    RIGHT = 39
    DOWN = 40
    SELECT = 41

    PRINTSCREEN = 44
    INSERT = 45
    DELETE = 46
    HELP = 47
    D0 = 48
    D1 = 49
    D2 = 50
    D3 = 51
    D4 = 52
    D5 = 53
    D6 = 54
    D7 = 55
    D8 = 56
    D9 = 57

    A = 65
    B = 66
    C = 67
    D = 68
    E = 69
    F = 70
    G = 71
    H = 72
    I = 73
    J = 74
    K = 75
    L = 76
    M = 77
    N = 78
    O = 79
    P = 80
    Q = 81
    R = 82
    S = 83
    T = 84
    U = 85
    V = 86
    W = 87
    X = 88
    Y = 89
    Z = 90

    NUMPAD0 = 96
    NUMPAD1 = 97
    NUMPAD2 = 98
    NUMPAD3 = 99
    NUMAPD4 = 100
    NUMPAD5 = 101
    NUMPAD6 = 102
    NUMPAD7 = 103
    NUMPAD8 = 104
    NUMPAD9 = 105

    ASTERISK = 106
    PLUS = 107
    MINUS = 108
    PERIOD = 110
    FSLASH = 111

    F1 = 112
    F2 = 113
    F3 = 114
    F4 = 115
    F6 = 117
    F7 = 118
    F8 = 119
    F9 = 120
    F10 = 121
    F11 = 122
    F13 = 124
    F14 = 125
    F15 = 126
    F16 = 127
    F17 = 128
    F18 = 129
    F19 = 130
    F20 = 131
    F21 = 132
    F22 = 133
    F23 = 134
    F24 = 135

    NUMLOCK = 144
    SCROLL = 145

    RSHIFT = 161
    LCONTROL = 162
    RCONTROL = 163
    LMENU = 164
    RMENU = 165

    EQUAL = 187
    COMMA = 188
    LBRACK = 189
    PERIOD2 = 190
    FSLASH2 = 191
    TILDE = 192

    LBRACK2 = 219
    FSLASH3 = 220
    RBRACK = 221
    APOSTRAPHE = 222
    
    def getKey(self, val):
        for key in Keys:
            if key == val:
                return key
        
        return None
