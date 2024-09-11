import sys
import pyautogui as pag
import threading
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import keyboard

class MouseMoverApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.bot_running = False
        self.init_ui()
        self.setWindowTitle("Mouse Mover Bot")
        self.setGeometry(100, 100, 400, 300)

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        self.setStyleSheet("""
            QMainWindow {
                font-family: 'Courier New', Courier, monospace;
                background-color: #000000;
            }
            QLabel {
                color: #00FF00;
                font-size: 18px;
                text-align: center;
            }
            QWidget {
                background-color: #000000;
                border: 2px solid #00FF00;
                border-radius: 12px;
                padding: 20px;
                width: 350px;
                margin: 0 auto;
            }
            QPushButton {
                background-color: #00FF00;
                border: none;
                color: #000000;
                padding: 12px 24px;
                font-size: 16px;
                margin: 10px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #00CC00;
            }
            QPushButton:pressed {
                background-color: #009900;
            }
            QLabel.notice {
                margin-top: 20px;
                color: #00FF00;
                font-size: 16px;
            }
        """)
        
        self.label = QLabel("Mouse Mover Bot")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)
        
        self.start_button = QPushButton("Start Bot")
        self.start_button.clicked.connect(self.start_bot)
        self.layout.addWidget(self.start_button)
        
        self.stop_button = QPushButton('Stop Bot or press "q"')
        self.stop_button.clicked.connect(self.stop_bot)
        self.layout.addWidget(self.stop_button)
        
        self.notice_label = QLabel("")
        self.notice_label.setObjectName("notice")
        self.layout.addWidget(self.notice_label)

    def start_bot(self):
        if not self.bot_running:
            self.bot_running = True
            self.notice_label.setText("Bot is running...")
            self.thread = threading.Thread(target=self.move_mouse)
            self.thread.start()

    def stop_bot(self):
        if self.bot_running:
            self.bot_running = False
            self.notice_label.setText("Bot stopped.")

    def move_mouse(self):
        x, y = pag.position()
        while self.bot_running:
            x += 200
            y += 200
            pag.moveTo(x, y)
            if x > 1900:
                x = 0
            if y > 1000:
                y = 0
            time.sleep(2)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.stop_bot()
        super().keyPressEvent(event)

def stop_bot_on_q():
    app = QApplication(sys.argv)
    main_window = MouseMoverApp()
    main_window.show()
    keyboard.on_press_key("q", lambda _: main_window.stop_bot())
    sys.exit(app.exec_())

if __name__ == '__main__':
    stop_bot_on_q()
