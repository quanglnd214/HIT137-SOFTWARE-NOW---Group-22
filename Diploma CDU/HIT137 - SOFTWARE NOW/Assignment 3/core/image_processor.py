from __future__ import annotations

class ImageProcessor:
    """Gives the app image processing functions.

    This class will include ways to:
        - Change colours to grayscale
        - Blurring
        - Finding edges
        - Changing the brightness and contrast
        - Rotation, flipping, and resizing
    All methods should:
        - Take photos as numpy arrays in OpenCV BGR format
        - Send back photographs that have been processed in BGR format
    """

    def to_grayscale(self, image):
        pass

    def blur(self, image, intensity: int):
        pass

    def edge_detection(self, image):
        pass

    def adjust_brightness(self, image, value: int):
        pass

    def adjust_contrast(self, image, value: float):
        pass

    def rotate(self, image, angle: int):
        pass

    def flip(self, image, mode: str):
        pass

    def resize(self, image, scale: int):
        pass