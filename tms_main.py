from PyQt5 import uic, QtGui, QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QStyleFactory, QDialog, QGridLayout, QFormLayout, \
    QTableWidgetItem
import resources
import psycopg2


class TMSMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.window = uic.loadUi("tms_main_window.ui", self)
        self.menu_button.clicked.connect(self.handle_menu)
        self.profile_button.clicked.connect(self.handle_profile_button)
        self.dashboard_button.clicked.connect(self.handle_dashboard_button)
        self.create_task_button.clicked.connect(self.handle_create_task)
        self.save_task_button.clicked.connect(self.save_button_handle)
        self.refresh_button.clicked.connect(self.refresh_button_handle)
        self.tb.itemChanged.connect(self.handle_tb_activate)
        self.tb.clicked.connect(self.handle_table_cleck)
        self.next_task_id = None

        lay = QFormLayout()
        # self.task_view_frame.setLayout(lay)
        # self.task_view_frame.setAlignment(Qt.AlignLeft)

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

        self.load_user_data()

    def handle_table_cleck(self, item):
        print(item.column(), item.row())

    def handle_menu(self):
        print(self.left_body_frame.width())
        if self.left_body_frame.width() == 210:
            self.left_body_frame.setMaximumWidth(88)
            self.left_body_frame.setMinimumWidth(88)
        else:
            self.left_body_frame.setMaximumWidth(210)
            self.left_body_frame.setMinimumWidth(210)

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

    def handle_create_task(self):
        dia = CreateTaskDialog(self)
        dia.show()
        row_position = self.tb.rowCount()
        self.tb.insertRow(row_position)
        self.tb.setItem(row_position, 0, QTableWidgetItem(str(self.next_task_id)))
        task_title = "Task"
        task_description = "task_description"
        created_at = "2000-01-01"
        updated_at = "2000-01-01"
        status = 'False'
        query = f"INSERT INTO task (task_id, task_title, task_description, created_at, updated_at, status, is_deleted) VALUES('{self.next_task_id}','{task_title}', '{task_description}', '{created_at}', '{updated_at}', '{status}', '{False}');"
        self.next_task_id += 1
        print(query)
        # self.cur.execute(query)
        # self.load_user_data()
        print('load data into table')
        # label1 = QtWidgets.QLabel(self.task_view_frame)
        # label1.setAlignment(Qt.AlignLeft)
        # label1.setText('Hi there')
        # label1.show()

    def load_user_data(self):
        query = "SELECT * From task;"
        self.cur.execute(query)
        result = self.cur.fetchall()
        # print(result)
        for record in result:
            row_position = self.tb.rowCount()
            self.tb.insertRow(row_position)
            # self.tb.setItem(row_position, 0, QTableWidgetItem(str(record[0])))

            self.tb.setItem(row_position, 0, QTableWidgetItem(str(record[0])))
            self.tb.setItem(row_position, 1, QTableWidgetItem(str(record[1])))
            self.tb.setItem(row_position, 2, QTableWidgetItem(str(record[2])))
            self.tb.setItem(row_position, 3, QTableWidgetItem(str(record[3])))
            self.tb.setItem(row_position, 4, QTableWidgetItem(str(record[4])))
            self.tb.setItem(row_position, 5, QTableWidgetItem(str(record[5])))

            self.next_task_id = record[0] + 1

    def save_button_handle(self):
        """
        Commit the Changes in Database.
        """
        print('Saving Data To DB.')
        self.conn.commit()

    def handle_tb_activate(self, item):
        """
        Update the changed value in database
        """
        print(f'text changed  {item.text()}')

        try:
            curr_row = self.tb.currentRow()
            # for row_id in range(5):
            task_id = self.tb.model().index(curr_row, 0)
            task_title = self.tb.model().index(curr_row, 1)
            task_description = self.tb.model().index(curr_row, 2)
            created_at = self.tb.model().index(curr_row, 3)
            updated_at = self.tb.model().index(curr_row, 4)
            status = self.tb.model().index(curr_row, 5)
            print(f'{task_id.data()}, {task_title.data()}', {task_description.data()}, {created_at.data()}, {updated_at.data()}, {status.data()})

            query = f"UPDATE task SET task_title = '{task_title.data()}', task_description = '{task_description.data()}' WHERE(task_id={task_id.data()});"
            print(query)
            self.cur.execute(query)

        except Exception as e:
            print(f'err {e}')
            self.cur.execute("ROLLBACK")

    def refresh_button_handle(self):
        self.tb.setRowCount(0)
        self.load_user_data()


class CreateTaskDialog(QDialog):
    def __init__(self, parent):
        super().__init__()

        self.window = uic.loadUi("create_task.ui", self)
        # Assigning Signals
        self.parent = parent
        self.create_button.clicked.connect(self.create_handle)
        self.cancel_button.clicked.connect(self.cancel_handle)
        # self.window.closeEvent = self.close_parent

    def create_handle(self):
        title = self.title_input.text()
        description = self.description_input.toPlainText()
        created_at = self.created_input.text()
        updated_at = self.updated_input.text()

        print(f'{title}, {description}, {created_at}, {updated_at}')

    def cancel_handle(self):
        self.close()

    def close_parent(self, event):
        self.parent.close()

