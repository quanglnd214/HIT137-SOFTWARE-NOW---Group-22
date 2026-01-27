from __future__ import annotations

from pathlib import Path
from typing import Optional, Tuple


class ImageModel:
    """Stores image state + metadata.

    The app should see pictures as OpenCV BGR (uint8) arrays.

    Responsibilities:
    - Keep the original image and the current functioning image.
    - Keep track of the file location and the "dirty" status (changes that haven't been saved).
    - Give minor utility methods to keep the GUI code clean.
    """
    def __init__(self) -> None:
        self.original_image = None
        self.current_image = None
        self.file_path: Optional[Path] = None
        self.dirty: bool = False

    def has_image(self) -> bool:
        """Return True if an image is currently loaded."""
        return self.current_image is not None

    def set_image(self, image, path: Optional[Path] = None) -> None:
        """Set a new image as both original and current image."""
        self.original_image = image
        self.current_image = image
        self.file_path = path
        self.dirty = False

    def apply_new_current(self, image) -> None:
        """Update the current image after processing."""
        self.current_image = image
        self.dirty = True

    def mark_saved(self, path: Optional[Path] = None) -> None:
        """Mark the image as saved."""
        if path is not None:
            self.file_path = path
        self.dirty = False

    def get_dimensions(self) -> Optional[Tuple[int, int]]:
        """Return image dimensions as (width, height)."""
        if self.current_image is None:
            return None
        height, width = self.current_image.shape[:2]
        return width, height