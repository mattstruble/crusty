#!/usr/bin/env python

# Copyright (c) 2016 Matt Struble. All Rights Reserved. 
#
# Use is subject to license terms.
#
# Author: Matt Struble
# Date: Sep. 1 2016
import os, sys

import colorama
from util.color import Color

class GraphicsDevice: #{
    """ Sets up the graphics environment for drawing to terminal """
    
    def __init__(self, w, h, title): #{
        
        colorama.init()

        os.system("mode {cols},{rows}".format(cols=w, rows=h))
        os.system("title " + title)
        #sys.stdout.write("\x1b]2;{name}\x07".format(name=title))
        #sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=h, cols=w))
        sys.stdout.write("\033[{col}m{char}\033[0m".format(col=Color.RGB(252, 127, 0).getShort(), char='YELLOW'))
        sys.stdout.write("\033[31;1;5mCOLOR\033[0m")
        sys.stdout.write("\033[44m\033[36mWORDS\033[0m\n")
    #}
#}
