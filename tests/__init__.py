import sys
import os
import platform

if platform.system() == 'Windows':
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "\\..\\crusty")
else:
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../crusty")
