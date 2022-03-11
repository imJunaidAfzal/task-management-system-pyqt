import re
import sys

from PyQt5 import uic
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMainWindow, QApplication, QStyleFactory, QDialog, QLabel, QWidget

from login import LoginMainWindow
from register_ui import Ui_RegisterationWin
import psycopg2

# class RegisterationWinSignals(Ui_RegisterationWin):
#     def __init__(self, win):
#         super().__init__()
#         self.setupUi(win)
#         self.retranslateUi(win)
#         self.submit_button.clicked.connect(self.submit_handle)
#         app = QApplication(sys.argv)
#         app.setStyle(QStyleFactory.create("Fusion"))
#         dialog = uic.loadUi('registration_done_dialog.ui', self)
#         dialog.exec()
#
#         try:
#             self.conn = psycopg2.connect(
#                 host='localhost',
#                 dbname='chat_db',
#                 user='postgres',
#                 password='12345678qQ',
#                 port=5432
#             )
#             self.cur = self.conn.cursor()
#             print('connect')
#
#             create_query = """
#             CREATE TABLE IF NOT EXISTS users(
#             First_Name  varchar(70),
#             Last_Name  varchar(70),
#             dob date,
#             gender varchar(1),
#             email varchar(80) PRIMARY KEY,
#             password varchar(40) NOT NULL
#             )
#             """
#             self.cur.execute(create_query)
#             self.conn.commit()
#             # self.conn.close()
#         except Exception as e:
#             print(f"not connect\n{e}")
#
#     def submit_handle(self):
#
#
#         fn = self.fn_input.text()
#         ln = self.ln_input.text()
#         dob = self.dob_input.text()
#         email = self.email_input.text()
#         gender = self.gender_input.currentText()
#         password = self.pass_input.text()
#         confirm_password = self.confirm_pass_input.text()
#
#         print(f'{fn} {ln}')
#         print(f'{dob}')
#         print(f'{email}')
#         print(f'{gender}')
#         print(f'{password}')
#         print(f'{confirm_password}')
#         if gender == 'Male':
#             gender = 'M'
#         elif gender == 'Female:':
#             gender = 'F'
#         else:
#             gender = 'O'
#
#         try:
#             query = f"INSERT INTO users (First_Name, Last_Name, dob, gender, email, password) VALUES(%s, %s, %s, %s, %s, %s); "
#             values = (fn, ln, dob, gender, email, password)
#             self.cur.execute(query, values)
#             self.conn.commit()
#         except psycopg2.errors.UniqueViolation:
#             print('already exist')
#             self.email_input.setStyleSheet("""
#             border : 1px solid ;
#             border-color : red;
#             background-color: rgba(204, 0, 0, 0.2);
#             """)
#             self.submit_button.setEnabled(False)

class RegisterMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.window = uic.loadUi("Register.ui", self)
        self.error_label.setHidden(True)
        print(self.window.submit_button.text())

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

            create_query = """
                    CREATE TABLE IF NOT EXISTS users(
                    First_Name  varchar(70),
                    Last_Name  varchar(70),
                    dob date,
                    gender varchar(1),
                    email varchar(80) PRIMARY KEY,
                    password varchar(40) NOT NULL
                    )
                    """
            self.cur.execute(create_query)
            self.conn.commit()
            # self.conn.close()
        except Exception as e:
            print(f"not connect\n{e}")

        # Assigning Signals
        self.submit_button.clicked.connect(self.submit_handle)
        self.email_input.textChanged.connect(self.email_text_chaned_handle)
        self.login_lbl.mousePressEvent = self.show_login

    def show_login(self, event):
        self.close()
        login_win = LoginMainWindow()
        login_win.show()

    def submit_handle(self):

        fn = self.fn_input.text()
        ln = self.ln_input.text()
        dob = self.dob_input.text()
        email = self.email_input.text()
        gender = self.gender_input.currentText()
        password = self.pass_input.text()
        confirm_password = self.confirm_pass_input.text()

        print(f'{fn} {ln}')
        print(f'{dob}')
        print(f'{email}')
        print(f'{gender}')
        print(f'{password}')
        print(f'{confirm_password}')
        if gender == 'Male' or gender == 'M':
            gender = 'M'
        elif gender == 'Female:' or gender == 'F':
            gender = 'F'
        else:
            gender = 'O'

        if not self.validate_field(self.fn_input):
            pass
        elif not self.validate_field(self.ln_input):
            pass
        elif not self.validate_email():
            pass
        elif not self.validate_password():
            pass
        else:

            try:
                query = f"INSERT INTO users (First_Name, Last_Name, dob, gender, email, password) \
                VALUES(%s, %s, %s, %s, %s, %s); "
                values = (fn, ln, dob, gender, email, password)
                self.cur.execute(query, values)
                self.conn.commit()
                dia = RegistrationDialog(self)
                dia.show()
                # self.close()

            except psycopg2.errors.UniqueViolation:
                print('already exist')
                self.email_input.setStyleSheet("""
                border : 1px solid ;
                border-color : red;
                background-color: rgba(204, 0, 0, 0.2);
                """)
                self.error_label.setText(f'{self.email_input.text()} already exists.')
                self.error_label.setHidden(False)
                self.submit_button.setEnabled(False)
                self.cur.execute("ROLLBACK")

    def email_text_chaned_handle(self):
        self.submit_button.setEnabled(True)
        self.email_input.setStyleSheet("")
        self.error_label.setHidden(True)

    def validate_email(self):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex,self.email_input.text()):
            return 1
        else:
            self.email_input.setStyleSheet("""
            border : 1px solid ;
            border-color : red;
            background-color: rgba(204, 0, 0, 0.2);
            """)
            self.error_label.setText('Invalid Email.')
            self.error_label.setHidden(False)
            return 0

    def validate_field(self, field):
        if len(field.text().strip()) < 3:
            field.setStyleSheet("""
            border : 1px solid ;
            border-color : red;
            background-color: rgba(204, 0, 0, 0.2);
            """)
            self.error_label.setText(f'{field.objectName()} must be at-least contains 3 characters. ')
            self.error_label.setHidden(False)
            return 0
        else:
            field.setStyleSheet("")
            self.error_label.setHidden(True)
            return 1

    def validate_password(self):
        if len(self.pass_input.text()) < 8:
            self.error_label.setText('Password must contains at-least 8 characters')
            self.error_label.setHidden(False)
            return 0
        elif self.pass_input.text() != self.confirm_pass_input.text():
            self.error_label.setText('Password do not match')
            self.error_label.setHidden(False)
            return 0
        else:
            self.error_label.setHidden(True)
            return 1


class RegistrationDialog(QDialog):
    def __init__(self, parent):
        super().__init__()

        self.window = uic.loadUi("registration_done_dialog.ui", self)
        # Assigning Signals
        self.parent = parent
        self.ok_button.clicked.connect(self.ok_handle)
        self.window.closeEvent = self.close_parent

    def ok_handle(self):
        self.close()
        self.parent.close()
        login_win = LoginMainWindow()
        login_win.show()

    def close_parent(self, event):
        self.parent.close()

