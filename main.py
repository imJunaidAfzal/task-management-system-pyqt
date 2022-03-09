from register import RegisterMainWindow
from login import LoginMainWindow


import sys
from PyQt5.QtWidgets import (
    QApplication,
    QStyleFactory,
)

from tms_main import TMSMainWindow

login_user = 'Guest'

if __name__ == '__main__':
    login_user = 'Guest'
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))

    reg_win = TMSMainWindow()
    reg_win.show()

    sys.exit(app.exec_())
