from register import RegisterMainWindow
from login import LoginMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QStyleFactory,
    QLabel,
    QProxyStyle,
    QStyle,
    QCommonStyle,
)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    # create the database information



    # bot = QtWidgets.QMainWindow()
    # ui = RegisterationWinSignals(bot)
    #
    # ui.setupUi(bot)
    # bot.show()
    reg_win = RegisterMainWindow()
    reg_win.show()

    sys.exit(app.exec_())
