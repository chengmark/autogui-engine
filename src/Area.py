from PIL import Image
from mss import mss
from mss.screenshot import ScreenShot
import cv2
import numpy


class Area:
    """
    represents a screen area
    """
    def __init__(self, top, left, width, height) -> None:
        self.top = top
        self.left = left
        self.width = width
        self.height = height

    def fromTLBR(top, left, bottom, right):
        """
        get Area from top, left, bottom, right
        """
        return Area(top, left, bottom - top, right - left)

    def is_match_pattern(self, pattern: numpy.ndarray) -> bool:
        """
        whether the given pattern matches current screen area
        """
        with mss() as sct:
            screen_shot = sct.grab(self.get_dimension())
            screen_array = self._to_gray_and_edged(screen_shot)
            return numpy.array_equal(pattern, screen_array)

    def get_pattern(self) -> numpy.ndarray:
        """
        get pattern of current screen area
        """
        with mss() as sct:
            screen_shot = sct.grab(self.get_dimension())
            pattern = self._to_gray_and_edged(screen_shot)
            return pattern

    def match_template(self, template: numpy.ndarray) -> tuple:
        """
        find object in current screen area, using template matching
        """
        with mss() as sct:
            screen_shot = sct.grab(self.get_dimension())
            screen_array = self._to_gray_and_edged(screen_shot)
            result = cv2.matchTemplate(screen_array, template, cv2.TM_CCOEFF)
            (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
            return (maxVal, maxLoc)


    def get_template(self) -> numpy.ndarray:
        """
        get current screen area in ndarray format, for template matching
        """
        with mss() as sct:
            screen_shot = sct.grab(self.get_dimension())
            return self._to_gray_and_edged(screen_shot)

    def save_image(self, img_name) -> None:
        """
        save current screen area as image
        """
        with mss() as sct:
            screen_shot = sct.grab(self.get_dimension())
            img_array = numpy.array(screen_shot)
            img = Image.fromarray(img_array)
            img.save(img_name)

    def save_template_image(self, img_name) -> None:
        """
        save current screen area as template image
        """
        img_array = self.get_template()
        img = Image.fromarray(img_array)
        img.save(img_name)

    def get_dimension(self):
        return {'top': self.top, 'left': self.left, 'width': self.width, 'height': self.height}

    def _to_gray_and_edged(self, screen_shot: ScreenShot) -> numpy.ndarray:
        """
        convert screenshot to gray scale and get edges by Canny algo
        """
        img_array = numpy.array(screen_shot)
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        return cv2.Canny(gray, 50, 200)
