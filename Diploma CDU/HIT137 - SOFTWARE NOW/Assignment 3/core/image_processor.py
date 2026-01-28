from __future__ import annotations

import cv2
import numpy as np

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

    @staticmethod
    def to_grayscale(image: np.ndarray) -> np.ndarray:
        """Convert BGR image to grayscale (returned as 3-channel BGR)."""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    @staticmethod
    def blur(image: np.ndarray, intensity: int = 5) -> np.ndarray:
        """Apply Gaussian blur. Intensity should be a positive odd number."""
        k = int(intensity)
        if k < 1:
            k = 1
        if k % 2 == 0:
            k += 1
        return cv2.GaussianBlur(image, (k, k), 0)

    @staticmethod
    def edge_detection(image: np.ndarray, t1: int = 80, t2: int = 160) -> np.ndarray:
        """Detect edges using Canny (returned as 3-channel BGR)."""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, t1, t2)
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    @staticmethod
    def adjust_brightness(self, image, value: int):
        pass

    @staticmethod
    def adjust_contrast(self, image, value: float):
        pass

    @staticmethod
    def rotate(self, image, angle: int):
        pass

    @staticmethod
    def flip(self, image, mode: str):
        pass

    @staticmethod
    def resize(self, image, scale: int):
        pass