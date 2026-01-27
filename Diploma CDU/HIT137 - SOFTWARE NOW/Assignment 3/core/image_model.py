from __future__ import annotations



class ImageModel:
    """Stores image state + metadata.

    The app should see pictures as OpenCV BGR (uint8) arrays.

    Responsibilities:
    - Keep the original image and the current functioning image.
    - Keep track of the file location and the "dirty" status (changes that haven't been saved).
    - Give minor utility methods to keep the GUI code clean.
    """
    def has_image(self) -> bool:
        pass

    def set_image(self, image, path=None) -> None:
        pass

    def apply_new_current(self, image) -> None:
        pass

    def mark_saved(self, path=None) -> None:
        pass

    def get_dimensions(self):
        pass