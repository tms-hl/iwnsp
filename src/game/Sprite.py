import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Image import Image
# XXX Änderung in einer Zeile
class Sprite(Image):
    '''
        Sprite ist ein Sprite
    '''
    def test(self):
        # Änderung später
        print("OK")
