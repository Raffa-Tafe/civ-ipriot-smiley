from smiley import Smiley
from blinkable import Blinkable
import time


class Happy(Smiley, Blinkable):
    def __init__(self):
        super().__init__()
        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws the mouth feature on a happy face.
        """
        mouth = [41, 46, 50, 51, 52, 53]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on a happy face.
        :param wide_open: Render eyes wide open or shut.
        """
        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else self.complexion()

    def blink(self, delay=0.25):
        """
        Blinks the smiley's eyes once.
        :param delay: Delay between blinks (in seconds)
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
