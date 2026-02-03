import tkinter as tk
from tkinter import messagebox


class EditorUI:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        # These will be created in setup_gui/setup_status_bar
        self.controls = None
        self.canvas = None
        self.blur_slider = None
        self.status_text = None

        # Build UI
        self.setup_window()
        self.setup_menu()
        self.setup_gui()
        self.setup_status_bar()
        self.bind_shortcuts()

        # Window
    def setup_window(self):
        self.root.title("HIT137 Image Editor")
        self.root.geometry("1000x700")

        # Menus
    def setup_menu(self):
        menubar = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.controller.open_file)
        file_menu.add_command(label="Save", command=self.controller.save_file)
        file_menu.add_command(label="Save As", command=self.controller.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        menubar.add_cascade(label="File", menu=file_menu)

        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.controller.undo_action)
        edit_menu.add_command(label="Redo", command=self.controller.redo_action)

        menubar.add_cascade(label="Edit", menu=edit_menu)

        # Help menu (optional but nice)
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menubar)

        # Main layout
    def setup_gui(self):

        # Sidebar (control panel)
        self.controls = tk.Frame(self.root, width=220, bg="gray85")
        self.controls.pack(side=tk.LEFT, fill=tk.Y)

        # Canvas (image display area)
        self.canvas = tk.Canvas(self.root, bg="gray30")
        self.canvas.pack(expand=True, fill=tk.BOTH)

        # Controls label
        tk.Label(
            self.controls,
            text="Filter Controls",
            font=("Arial", 12, "bold"),
            bg="gray85").pack(pady=10)

        # Slider (required: at least one adjustable effect)
        tk.Label(self.controls, text="Blur Intensity", bg="gray85").pack()
        self.blur_slider = tk.Scale(
            self.controls,
            from_=0,
            to=10,
            orient=tk.HORIZONTAL)
        self.blur_slider.pack(pady=5)

        # Filter buttons
        tk.Button(
            self.controls,
            text="Grayscale",
            command=self.controller.apply_grayscale).pack(pady=5, fill="x")
        tk.Button(
            self.controls,
            text="Blur",
            command=self.controller.apply_blur).pack(pady=5, fill="x")
        tk.Button(
            self.controls,
            text="Edge",
            command=self.controller.apply_edge).pack(pady=5, fill="x")

        # Invert Colours button (your extra controller function)
        tk.Button(
            self.controls,
            text="Invert Colours",
            command=self.controller.apply_invert).pack(pady=5, fill="x")

        # Status bar
    def setup_status_bar(self):
        self.status_text = tk.StringVar(value="Ready")
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_text,
            relief=tk.SUNKEN,
            anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def set_status(self, msg: str):
        if self.status_text is not None:
            self.status_text.set(msg)

        # Helpers the controller can use
    def get_blur_value(self) -> int:
        if self.blur_slider is None:
            return 0
        return int(self.blur_slider.get())

        # Shortcuts
    def bind_shortcuts(self):
        self.root.bind("<Control-o>", lambda e: self.controller.open_file())
        self.root.bind("<Control-s>", lambda e: self.controller.save_file())
        self.root.bind("<Control-Shift-S>", lambda e: self.controller.save_as_file())
        self.root.bind("<Escape>", lambda e: self.root.quit())

        # About popup
    def show_about(self):
        messagebox.showinfo(
            "About",
            "HIT137 Assignment 3 - Image Editor\n\n"
            "Built with Tkinter + OpenCV\n\n"
            "Features:\n"
            "- Open / Save / Save As\n"
            "- Undo / Redo\n"
            "- Grayscale\n"
            "- Blur (slider)\n"
            "- Edge Detection\n"
            "- Invert Colours\n")

