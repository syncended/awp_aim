import ctypes
from PIL import ImageGrab, ImageChops
from time import sleep
from threading import Thread


class Aim(Thread):

    def __init__(self):
        super().__init__()

        self.get_screen_size()
        self.stop = True

    def run(self):
        self.stop = False
        self.aim()


    def get_screen_size(self):
        size = ImageGrab.grab().size
        self.x = size[0]
        self.y = size[1]



    def aim(self):
        mouse_event = ctypes.windll.user32.mouse_event
        img1 = self.get_image()
        while not self.stop:
            img2 = self.get_image()
            if not self.compare(img1, img2):
                mouse_event(2, 0, 0, 0, 0)
                mouse_event(4, 0, 0, 0, 0)
                print('SGOOOOOOOOOOOOOOOOOOT')
                sleep(5)
                img2 = self.get_image()
                return

    def get_image(self):
        b = [self.x/2-2, self.y/2-2, self.x/2+2, self.y/2+2]
        shot = ImageGrab.grab(bbox=b)
        return shot

    def compare(self, im1, im2):
        return ImageChops.difference(im1, im2).getbbox() is None

    def _stop(self):
        self.stop = True