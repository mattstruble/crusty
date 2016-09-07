#! /usr/bin/env python

""" Provides common use variables and functionality """

# Author: Matt Struble
# Date: Sep. 6 2016
#---------------------------------------------------------------------
from sys import platform as _platform

WINDOWS = 0
LINUX   = 1
MACOSX  = 2

OSYSTEM = 0

if _platform == "linux" or _platform == "linux2":
    OSYSTEM = LINUX
elif _platform == "darwin":
    OSYSTEM = MACOSX
elif _platform == "win32":
    OSYSTEM = WINDOWS
