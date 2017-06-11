#!/usr/bin/env python

# Copyright (c) 2016 Matt Struble. All Rights Reserved. 
#
# Use is subject to license terms.
#
# Author: Matt Struble
# Date: Aug. 31 2016
import time, os
from graphics.graphicsdevice import GraphicsDevice

class Game: #{
    """ Handles initialization and core game loop. """
    
    FPS = 30.0
    SEC_PER_FRAME = 1.0/FPS

    def __init__(self, w='1000', h='300', title='Game'): #{

        self.gd = GraphicsDevice(w, h, title)
        
        print "ran game" 
        raw_input('')
    #}
        
    def run(): #{
        _initialize()
        _loadContent()
        loop()
    #}

    def _initialize(): #{
        pass
    #}

    def _loadContent(): #{
        pass
    #}

    def _loop(): #{
        previous = time.time()

        while True: #{
            current = time.time()
            dt = current - previous
            previous = current
            
            _processInput()
            _update(dt)
            _render()

            sleepTime = SEC_PER_FRAME - ( time.time() - current )
            if sleepTime > 0: #{
                time.sleep( sleepTime )
            #}
        #}
    #}
                 
    def _processInput(): #{
        pass
    #}

    def _update(dt): #{
        pass
    #}

    def _render(): #{
        # Clear terminal buffer
        os.system('cls' if os.name == 'nt' else 'clear')
        pass
    #}
