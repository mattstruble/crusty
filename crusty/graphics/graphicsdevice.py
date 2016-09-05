#! /usr/bin/env python

""" Sets up the graphics environment for drawing to terminal """

# Author: Matt Struble
# Date: Sep. 1 2016
#---------------------------------------------------------------------
import os, sys
import colorama

class GraphicsDevice: #{

    def __init__(self, w, h, title): #{
        
        colorama.init()

        os.system("mode {cols},{rows}".format(cols=w, rows=h))
        os.system("title " + title)
        #sys.stdout.write("\x1b]2;{name}\x07".format(name=title))
        #sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=h, cols=w))
        sys.stdout.write("\033[{col}m{char}\033[0m".format(col=31, char='RED'))
        sys.stdout.write("\033[38;5;38mCOLOR\033[0m")
    #}
#}
