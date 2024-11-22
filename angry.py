# angry.py
from smiley import Smiley

class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=self.RED)  # Pass red color
        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws the mouth feature on an angry smiley (slightly turned down to express anger).
        """
        mouth = [50, 42, 43, 44, 45, 53]  # Similar to the happy face, but the mouth will be flipped.
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on the angry smiley (eyes usually open for an angry face).
        """
        eyes = [9, 10, 18, 21, 13, 14]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else self.my_complexion
