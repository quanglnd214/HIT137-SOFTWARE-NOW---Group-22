import tkinter as tk
from tkinter import filedialog, messagebox
# These imports represent the files Members 1 and 4 will work on
# from models import HistoryManager
# from processor import ImageProcessor

class EditorApp:
    """
    Main Application Class (Member 2 & 1 focus).
    Demonstrates OOP Constructor and Class Interaction.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("HIT137 Assignment 3 - Image Editor") [cite: 26]
        self.root.geometry("1000x700") [cite: 26]

        # API CONNECTIONS:
        # self.processor = ImageProcessor()  # Link to Member 4's work
        # self.history = HistoryManager()    # Link to Member 1's work

        self.setup_menu()      # Member 3's task
        self.setup_gui()       # Member 2's task
        self.setup_status_bar() # Member 2's task

    def setup_menu(self):
        """Requirement: Menu Bar with File and Edit menus[cite: 27]."""
        menubar = tk.Menu(self.root)
        
        # File Menu (Member 3)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file) [cite: 27, 31]
        file_menu.add_command(label="Save", command=self.save_file) [cite: 27, 31]
        file_menu.add_command(label="Save As", command=self.save_as_file) [cite: 27, 31]
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit) [cite: 27]
        menubar.add_cascade(label="File", menu=file_menu)

        # Edit Menu (Member 3)
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.undo_action) [cite: 27]
        edit_menu.add_command(label="Redo", command=self.redo_action) [cite: 27]
        menubar.add_cascade(label="Edit", menu=edit_menu)

        self.root.config(menu=menubar)

    def setup_gui(self):
        """Requirement: Image Display and Control Panel[cite: 28, 29]."""
        # Sidebar for filters (Member 2)
        self.controls = tk.Frame(self.root, width=200, bg="gray80") [cite: 29]
        self.controls.pack(side=tk.LEFT, fill=tk.Y)

        # Canvas for Image Display (Member 2)
        self.canvas = tk.Canvas(self.root, bg="gray30") [cite: 28]
        self.canvas.pack(expand=True, fill=tk.BOTH)

        # EXAMPLE: Member 4's Filter Trigger (Slider)
        tk.Label(self.controls, text="Blur Intensity").pack()
        self.blur_slider = tk.Scale(self.controls, from_=0, to=10, orient=tk.HORIZONTAL) [cite: 33]
        self.blur_slider.pack()

    def setup_status_bar(self):
        """Requirement: Status Bar for image info[cite: 30]."""
        self.status_text = tk.StringVar(value="Ready")
        status_bar = tk.Label(self.root, textvariable=self.status_text, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    # --- API STUBS FOR MEMBERS 3 & 4 TO FILL ---
    def open_file(self):
        """Triggers file dialog for JPG, PNG, BMP[cite: 31, 32]."""
        # Member 3: Implement file dialog logic here
        pass

    def save_file(self):
        """Saves current image."""
        # Member 3: Implement save logic here
        pass
    
    def save_as_file(self):
        """Saves image with new name[cite: 27]."""
        # Member 3: Implement Save As logic here
        pass

    def undo_action(self):
        """Reverts last filter application[cite: 27]."""
        # Member 1: Connect to HistoryManager here
        pass

    def redo_action(self):
        """Re-applies previously undone action[cite: 27]."""
        # Member 1: Connect to HistoryManager here
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = EditorApp(root)
    root.mainloop()
