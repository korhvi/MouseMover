# MouseMoverPage

MouseMoverPage is a simple desktop application designed to automatically move the mouse pointer at regular intervals. This tool is useful for keeping your computer awake or preventing idle mode.

<p align="center">
  <img src="https://github.com/user-attachments/assets/974ac5be-0c8b-4c85-805d-e731d361771c" alt="MouseMoverPage Screenshot"/>
</p>

## Features

- Start and stop the mouse mover bot with a click of a button.
- Moves the mouse pointer in a predefined pattern across the screen.
- Option to stop the bot using the "q" key.
- User-friendly interface with a retro console-style design.

## Files

- `build/app`: Contains build files.
- `dist/app.exe`: The compiled executable for running the application.
- `.gitattributes`: Git attributes file for managing repository settings.
- `.gitignore`: Git ignore file for excluding specific files and directories.
- `LICENSE`: The license file for the project.
- `README.md`: This README file.
- `app.py`: The main Python script for the application.
- `app.spec`: The PyInstaller specification file for building the executable.

## Getting Started

### Prerequisites

- Python 3.x
- PyQt5
- PyAutoGUI
- Keyboard

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/MouseMoverPage.git
    cd MouseMoverPage
    ```

2. Install the required dependencies:

    ```bash
    pip install pyqt5 pyautogui keyboard
    ```

3. Run the application:

    ```bash
    python app.py
    ```

### Usage

- You can run the application directly by opening the `app.exe` file located in the `dist` folder.
- Alternatively, run the application from the source code:

 1. Launch the application.
 2. Click the "Start Bot" button to begin moving the mouse.
 3. Stop the movement by clicking the "Stop Bot" button or pressing the "q" key.

## Building the Executable

To build an executable for your application, use the following command:

```bash
pyinstaller --onefile --windowed app.spec
