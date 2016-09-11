#! /usr/bin/env python

""" Generates hooks and listens for windows keyboard events. """

# Author: Matt Struble
# Date: Sep. 11 2016
# Code adapted from: https://github.com/boppreh/keyboard/
#---------------------------------------------------------------------

import ctypes
from ctypes import wintypes
from keyboardevent import KeyboardEvent

def listen(handler):
	""" Listens for events and passes them to handler. """
	from ctypes import windll, CFUNCTYPE, POINTER, c_int, c_void_p, byref
	import atexit
	event_types = {0x100: KeyboardEvent.KEY_DOWN, #WM_KeyDown for normal keys
			0x101: KeyboardEvent.KEY_UP, #WM_KeyUp for normal keys
			0x104: KeyboardEvent.KEY_DOWN, # WM_SYSKEYDOWN, used for Alt key.
			0x105: KeyboardEvent.KEY_UP, # WM_SYSKEYUP, used for Alt key.
			}
	def low_level_handler(nCode, wParam, lParam):
		"""
		Processes a low level Windows keyboard event.
		"""
		event = KeyboardEvent(event_types[wParam], lParam[0] & 0xFFFFFFFF, 
                                        lParam[1], lParam[2] == 32, lParam[3])
		handler(event)
		#Be nice, return next hook
		return windll.user32.CallNextHookEx(hook_id, nCode, wParam, lParam)
	
	# Low level handler signature.
	CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
	# Convert the Python handler into C pointer.
	pointer = CMPFUNC(low_level_handler)
	
	windll.kernel32.GetModuleHandleW.restype = wintypes.HMODULE
	windll.kernel32.GetModuleHandleW.argtypes = [wintypes.LPCWSTR]
	
	# Hook both key up and key down events for common keys (non-system).
	hook_id = windll.user32.SetWindowsHookExA(0x00D, pointer,
						windll.kernel32.GetModuleHandleW(None), 0)

	# Register to remove the hook when the interpreter exits.
	atexit.register(windll.user32.UnhookWindowsHookEx, hook_id)
	while True:
		msg = windll.user32.GetMessageW(None, 0, 0,0)
		windll.user32.TranslateMessage(byref(msg))
		windll.user32.DispatchMessageW(byref(msg))

