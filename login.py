from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog
import psycopg2

from tms_main import TMSMainWindow


class LoginMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.window = uic.loadUi("login_window.ui", self)
        self.login_user = 'Guest'
        self.error_label.setHidden(True)
        try:
            self.connection = psycopg2.connect(
                host='localhost',
                dbname='chat_db',
                user='postgres',
                password='12345678qQ',
                port=5432
            )

            self.cursor = self.connection.cursor()
        except Exception as e:
            print('Print DB connection failed')

        # Signals
        self.login_button.clicked.connect(self.login_handle)
        self.create_account_label.mousePressEvent = self.create_account_handle
        self.email_input.textChanged.connect(self.email_text_handle)
        self.password_input.textChanged.connect(self.password_text_handle)

    def login_handle(self):
        email = self.email_input.text()
        password = self.password_input.text()

        query = f"SELECT email, password FROM users where(email='{email}');"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print(result)
        if len(result) == 0:
            self.error_label.setText('No user found against provided email.')
            self.error_label.setHidden(False)
            self.email_input.setStyleSheet("""
            border : 1px solid ;
            border-color : red;
            background-color: rgba(204, 0, 0, 0.2);
            """)
        elif result[0][1] == password:
            query = f"SELECT first_name, last_name FROM users where(email='{email}');"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.login_user = result[0][0] + ' ' + result[0][1]
            print('Login successful')
            self.error_label.setHidden(True)
            self.password_input.setStyleSheet("")
            self.email_input.setStyleSheet("")
            dia = LoginDialog(self)
            dia.show()
            # self.log_in_user =
        else:
            self.error_label.setText('Invalid Password.')
            self.error_label.setHidden(False)
            self.password_input.setStyleSheet("""
            border : 1px solid ;
            border-color : red;
            background-color: rgba(204, 0, 0, 0.2);
            """)

    def email_text_handle(self):
        self.email_input.setStyleSheet("")

    def password_text_handle(self):
        self.password_input.setStyleSheet("")

    def create_account_handle(self, event):
        # To avoid circular import
        from register import RegisterMainWindow
        self.close()
        reg_win = RegisterMainWindow()
        reg_win.show()


class LoginDialog(QDialog):
    def __init__(self, parent):
        super().__init__()

        self.window = uic.loadUi("login_dialog.ui", self)
        # Assigning Signals
        self.parent = parent
        self.ok_dialog_button.clicked.connect(self.ok_dialog_handle)
        self.window.closeEvent = self.close_parent

    def ok_dialog_handle(self):
        self.close()
        self.parent.close()
        tms_win = TMSMainWindow()
        tms_win.name_label.setText(self.parent.login_user)
        tms_win.show()

    def close_parent(self, event):
        self.parent.close()

