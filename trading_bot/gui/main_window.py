# main_window.py базовая структура GUI-окна

from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Binary Options Bot')
