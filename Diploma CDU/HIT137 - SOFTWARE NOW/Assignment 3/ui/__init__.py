# UI package for HIT137 Assignment 3

     def open_file(self):
        """
        Let the user select an image file and open it.
        
   
        """
        # File dialog to select image
        file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.png *.bmp")]
        )

        if not file_path:
            return  # User cancelled

        # Read the image using OpenCV
        image = cv2.imread(file_path)
        if image is None:
            messagebox.showerror("Error", "Cannot load image.")
            return

        # Update the model and display on canvas
        self.model.apply_new_current(image)
        self.display_image(image)
        self.current_file_path = file_path
        self.unsaved_changes = False

        # Update status bar with filename and dimensions
        h, w = image.shape[:2]
        self.status_text.set(f"Opened: {file_path} ({w}x{h})")

    def save_file(self):
        """
        Save the current image to disk.
        If the file has never been saved, delegate to save_as_file().
    
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
    
        """
        file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[
            ("PNG files", "*.png"),
            ("JPEG files", "*.jpg"),
            ("BMP files", "*.bmp") ]
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
    
        """
        image = self.history.redo(self.model.current_image)
        if image is not None:
            self.model.apply_new_current(image)
            self.display_image(image)
            self.status_text.set("Redo performed")
        else:
            self.status_text.set("Nothing to redo")

    


