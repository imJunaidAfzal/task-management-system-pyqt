from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QStyleFactory, QDialog
import resources
import psycopg2


class TMSMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.window = uic.loadUi("tms_main_window.ui", self)
        self.menu_button.clicked.connect(self.handle_menu)
        self.profile_button.clicked.connect(self.handle_profile_button)
        self.dashboard_button.clicked.connect(self.handle_dashboard_button)

        try:
            self.conn = psycopg2.connect(
                host='localhost',
                dbname='chat_db',
                user='postgres',
                password='12345678qQ',
                port=5432
            )
            self.cur = self.conn.cursor()
            print('connect')

        except Exception as e:
            print(f"not connect\n{e}")

    def handle_menu(self):
        print(self.left_body_frame.width())
        if self.left_body_frame.width() == 200:
            self.left_body_frame.setMaximumWidth(88)
        else:
            self.left_body_frame.setMaximumWidth(200)

    def handle_dashboard_button(self):
        self.dashboard_frame.setStyleSheet("""
        background-color: rgba(80, 80, 80, 193);
        """)
        self.profile_frame.setStyleSheet("")

    def handle_profile_button(self):
        self.profile_frame.setStyleSheet("""
        background-color: rgba(80, 80, 80, 193);
        """)
        self.dashboard_frame.setStyleSheet("")
