from sense_hat import SenseHat
import time


class Smiley:
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLANK = (0, 0, 0)
    BLUE = (0, 0, 255)


    def __init__(self, complexion=None):
        # Default to YELLOW if no complexion is provided
        self.my_complexion = complexion if complexion else self.YELLOW
        self.sense_hat = SenseHat()

        X = self.my_complexion  # Use the assigned complexion
        O = self.BLANK
        self.pixels = [
            O, X, X, X, X, X, X, O,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            O, X, X, X, X, X, X, O,
        ]

    def draw_mouth(self):
        """
        Draws the mouth feature on a happy face.
        """
        mouth = [41, 46, 50, 51, 52, 53]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on a smiley
        :param wide_open: Render eyes wide open or shut
        """
        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            if wide_open:
                self.pixels[pixel] = self.BLANK
            else:
                self.pixels[pixel] = self.my_complexion

    def complexion(self):
        """
        Returns the complexion color for the smiley.
        """
        return self.my_complexion


    def initialize_face(self):
        """
        Initializes the face with a complexion border.
        """
        complexion_color = self.complexion()
        for i in range(64):
            if i not in [0, 7, 56, 63]:  # Inner border pixels
                self.pixels[i] = complexion_color

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
    def dim_display(self, dimmed=True):
        """
        Set the SenseHat's light intensity to low (True) or high (False).
        :param dimmed: Dim the display if True, otherwise don't dim.
        """
        self.sense_hat.low_light = dimmed

    def show(self):
        """
        Show the smiley on the screen.
        """
        self.sense_hat.set_pixels(self.pixels)
