from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class LoginMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.window = uic.loadUi("login_window.ui", self)
        self.error_label.setHidden(True)

