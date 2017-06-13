#!/usr/bin/env python

# Copyright (c) 2016 Matt Struble. All Rights Reserved. 
#
# Use is subject to license terms.
#
# Author: Matt Struble
# Date: Aug. 31 2016
import time, os
from graphics.graphicsdevice import GraphicsDevice
from input.keyboard import Keyboard, Keys

class Game: #{
    """ Handles initialization and core game loop. """
    
    FPS = 30.0
    SEC_PER_FRAME = 1.0/FPS

    def __init__(self, w='1000', h='300', title='Game'): 
        self.gd = GraphicsDevice(w, h, title)
        self.run()
    
    def run(self): 
        self._initialize()
        self._loadContent()
        self._loop()
    

    def _initialize(self): 
        Keyboard.initialize()
        self.running = True
    
    def _terminate(self):
        Keyboard.terminate()
        self.running = False

    def _loadContent(self): 
        pass
    

    def _loop(self): 
        previous = time.time()

        while self.running: 
            current = time.time()
            dt = current - previous
            previous = current
            
            self._processInput()
            self._update(dt)
            self._render()

            sleepTime = self.SEC_PER_FRAME - ( time.time() - current )
            if sleepTime > 0: 
                time.sleep( sleepTime )

                 
    def _processInput(self):
        if Keyboard.released(Keys.ESCAPE):
            self._terminate()

    def _update(self, dt): 
        Keyboard._update()
    
    def _render(self): 
        # Clear terminal buffer
        pass #os.system('cls' if os.name == 'nt' else 'clear')
    
