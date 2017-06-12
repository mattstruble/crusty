from _keyboardlistener import KeyboardListener as __KeyboardListener
from crusty.eventhandler import EventHandler

__kbListener = __KeyboardListener()
__kbListener.addHandler(EventHandler.eventHandler)
__kbListener.start()