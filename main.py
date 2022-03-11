import psycopg2

from register import RegisterMainWindow
from login import LoginMainWindow


import sys
from PyQt5.QtWidgets import (
    QApplication,
    QStyleFactory,
)

from tms_main import TMSMainWindow

try:
    conn = psycopg2.connect(
        host='localhost',
        dbname='chat_db',
        user='postgres',
        password='12345678qQ',
        port=5432
    )
    cur = conn.cursor()
    print('connect')

    create_query_user = """
            CREATE TABLE IF NOT EXISTS users(
            First_Name  varchar(70),
            Last_Name  varchar(70),
            dob date,
            gender varchar(1),
            email varchar(80) PRIMARY KEY,
            password varchar(40) NOT NULL
            )
            """
    cur.execute(create_query_user)

    create_query_task = """
                CREATE TABLE IF NOT EXISTS task(
                task_id int PRIMARY KEY,
                task_title  varchar(70),
                task_description  varchar(300),
                created_at date,
                updated_at date,
                status bool,
                is_deleted bool
                )
                """
    cur.execute(create_query_task)
    conn.commit()
except Exception as exp:
    print(f'Failed to connect to database. {exp}')


if __name__ == '__main__':
    login_user = 'Guest'
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))

    reg_win = TMSMainWindow()
    reg_win.show()

    sys.exit(app.exec_())
