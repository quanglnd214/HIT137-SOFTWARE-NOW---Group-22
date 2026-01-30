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
    def adjust_brightness(image: np.ndarray, value: int) -> np.ndarray:
        """Adjust image brightness."""
        return cv2.convertScaleAbs(image, alpha=1.0, beta=value)

    @staticmethod
    def adjust_contrast(image: np.ndarray, value: float) -> np.ndarray:
        """Adjust image contrast."""
        return cv2.convertScaleAbs(image, alpha=value, beta=0)

    @staticmethod
    def rotate(image: np.ndarray, angle: int) -> np.ndarray:
        """Rotate image by 90, 180 or 270 degrees."""
        angle = angle % 360
        if angle == 90:
            return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        if angle == 180:
            return cv2.rotate(image, cv2.ROTATE_180)
        if angle == 270:
            return cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        return image

    @staticmethod
    def flip(image: np.ndarray, mode: str) -> np.ndarray:
        """Flip image horizontally or vertically."""
        if mode == "h":
            return cv2.flip(image, 1)
        if mode == "v":
            return cv2.flip(image, 0)
        return image

    @staticmethod
    def resize(image: np.ndarray, scale: int) -> np.ndarray:
        """Resize image by scale percentage."""
        scale = max(10, min(scale, 300))
        height, width = image.shape[:2]
        new_w = int(width * scale / 100)
        new_h = int(height * scale / 100)
        return cv2.resize(image, (new_w, new_h))