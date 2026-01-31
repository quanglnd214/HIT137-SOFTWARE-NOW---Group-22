# UI package for HIT137 Assignment 3

def save_file(self):
    """
    Save the current image to disk.
    If the file has never been saved, delegate to save_as_file().
    This is a UI method because it handles file dialogs and user interaction.
    """
    if self.current_file_path is None:
        # Ask user where to save
        self.save_as_file()
    else:
        # Save to existing path
        cv2.imwrite(self.current_file_path, self.current_image)
        self.unsaved_changes = False  # mark as saved
        print(f"Saved: {self.current_file_path}")


def save_as_file(self):
    """
    Open a "Save As" dialog to let the user choose a path and filename.
    Updates current_file_path and resets unsaved_changes flag.
    UI method: handles user interaction and dialogs.
    """
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[
            ("PNG files", "*.png"),
            ("JPEG files", "*.jpg"),
            ("BMP files", "*.bmp")
        ]
    )

    if not file_path:
        return  # User cancelled

    # Save image to chosen path
    cv2.imwrite(file_path, self.current_image)
    self.current_file_path = file_path
    self.unsaved_changes = False
    print(f"Saved as: {file_path}")


def undo_action(self):
    """
    Undo the last image operation.
    Calls HistoryManager to retrieve the previous image state.
    Updates the canvas and status bar.
    UI method because it interacts with user (menu/shortcut) and canvas.
    """
    image = self.history.undo(self.model.current_image)
    if image is not None:
        self.model.apply_new_current(image)
        self.display_image(image)
        self.status_text.set("Undo performed")
    else:
        self.status_text.set("Nothing to undo")


def redo_action(self):
    """
    Redo the last undone operation.
    Calls HistoryManager to retrieve the next image state.
    Updates the canvas and status bar.
    UI method because it interacts with user (menu/shortcut) and canvas.
    """
    image = self.history.redo(self.model.current_image)
    if image is not None:
        self.model.apply_new_current(image)
        self.display_image(image)
        self.status_text.set("Redo performed")
    else:
        self.status_text.set("Nothing to redo")

