# HIT137 Assignment 3 - Group 22: Python Image Editor

A professional desktop image processing application built with **Python**, **Tkinter**, and **OpenCV**. This project follows the Model-View-Controller (MVC) architecture to provide a robust and extensible editing experience.

## 📝 Project Overview
This application allows users to perform standard image manipulations, apply advanced filters, and manage file states with a full Undo/Redo history. It was developed as a collaborative effort to demonstrate proficiency in OOP, GUI design, and computer vision libraries.

## 👥 Team Members & Contributions

| Member | Focus Area | Key Deliverables |
| :--- | :--- | :--- |
| **Member 1** | **Core / OOP** | Developed `ImageModel` and `HistoryManager`. Implemented the state management and Undo/Redo logic. |
| **Member 2** | **GUI (Tkinter)** | Designed the main window layout, sidebar controls, and dynamic Canvas rendering. |
| **Member 3** | **Menu & Files** | Built the menu system, file I/O (Open/Save/Save As), and unsaved change protection. |
| **Member 4** | **Processing & QA** | Implemented 8+ OpenCV filters/transformations, performed edge-case testing, and finalized documentation. |

---

## 🚀 Key Features

### 🛠 Image Processing (OpenCV)
* **Color Operations:** Grayscale conversion.
* **Enhancements:** Adjustable Brightness and Contrast.
* **Filters:** Gaussian Blur (with slider intensity) and Canny Edge Detection.
* **Geometric Transforms:** * Rotation (90° clockwise).
  * Flipping (Horizontal and Vertical).
  * Resizing (Presets and **Manual % Input**).

### 🖥 User Interface (Tkinter)
* **Canvas Display:** Centered image rendering that updates in real-time.
* **Control Panel:** Intuitive sidebar with sliders for parameter-based filtering.
* **Status Bar:** Real-time feedback on file paths, image dimensions, and action history.
* **Keyboard Shortcuts:** Support for standard shortcuts (e.g., Undo/Redo/Save).

### 💾 File & State Management
* **File Types:** Supports `.jpg`, `.png`, and `.bmp`.
* **Undo/Redo:** Unlimited history stack to revert or re-apply changes.
* **Validation:** Dialog alerts for unsaved changes and invalid file inputs.

---

## 📂 Project Structure
```text
├── core/
│   ├── history.py          # History stack logic (Member 1)
│   ├── image_model.py      # Image data container (Member 1)
│   └── image_processor.py  # OpenCV implementation (Member 4)
├── ui/
│   ├── ui.py
├── main.py                 # App Controller & UI (Member 2 & 3)
├── requirements.txt        # External dependencies
└── README.md               # Project documentation
```
## 🛠 Installation & Usage
### Clone the Repository:

git clone [https://github.com/quanglnd214/HIT137-SOFTWARE-NOW---Group-22].git

### Install Dependencies:

pip install opencv-python pillow numpy

### Run the App:

python main.py

### 🧪 Testing & Verification

The application has been rigorously tested to ensure cross-platform stability and functional accuracy.

### 1. Functional Testing
* **Open Function:** Verified successful loading of `.png`, `.jpg`, and `.bmp`. Status bar correctly displays image path and resolution.
* **Filter Suite:** All 8 functions (Grayscale, Blur, Edge, Brightness, Contrast, Rotate, Flip, Resize) tested for pixel accuracy and real-time canvas updates.
* **Undo/Redo:** Stress-tested with 10+ consecutive operations to ensure memory stability and state recovery.
* **Save/Save As:** Verified that processed images are correctly encoded and written to disk. "Save As" successfully prompts for new file names.

### 2. Compatibility & IDE Support
We confirmed consistent behavior across the following environments:
* **PyCharm:** Successfully tested using the `venv` interpreter. GUI components render correctly in the scientific and standard views.
* **VS Code:** Verified using the Microsoft Python extension. Terminal execution and debugging work without pathing errors.
* **Multi-Platform:** Tested on Windows and macOS to ensure Tkinter window scaling remains user-friendly across different operating systems.

### 3. Error Handling
* **Gatekeeper Logic:** Prevented application crashes by implementing checks that block filters from running if no image is loaded.
* **Input Validation:** Manual resize inputs are restricted to positive numbers only, with error pop-ups for invalid text entries.

