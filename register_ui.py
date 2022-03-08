# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisterationWin(object):
    def setupUi(self, RegisterationWin):
        RegisterationWin.setObjectName("RegisterationWin")
        RegisterationWin.resize(414, 698)
        RegisterationWin.setMinimumSize(QtCore.QSize(414, 698))
        RegisterationWin.setMaximumSize(QtCore.QSize(746, 806))
        RegisterationWin.setWindowOpacity(0.97)
        RegisterationWin.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(RegisterationWin)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_frame = QtWidgets.QFrame(self.centralwidget)
        self.top_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.top_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.welcome_lbl = QtWidgets.QLabel(self.top_frame)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.welcome_lbl.setFont(font)
        self.welcome_lbl.setObjectName("welcome_lbl")
        self.verticalLayout_2.addWidget(self.welcome_lbl, 0, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(self.top_frame)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.register_lbl = QtWidgets.QLabel(self.top_frame)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.register_lbl.setFont(font)
        self.register_lbl.setObjectName("register_lbl")
        self.verticalLayout_2.addWidget(self.register_lbl, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.top_frame)
        self.mid_frame = QtWidgets.QFrame(self.centralwidget)
        self.mid_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mid_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mid_frame.setObjectName("mid_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.mid_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.mid_frame)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.fn_lbl = QtWidgets.QLabel(self.frame)
        self.fn_lbl.setObjectName("fn_lbl")
        self.verticalLayout_3.addWidget(self.fn_lbl, 0, QtCore.Qt.AlignRight)
        self.lb_lbl = QtWidgets.QLabel(self.frame)
        self.lb_lbl.setObjectName("lb_lbl")
        self.verticalLayout_3.addWidget(self.lb_lbl, 0, QtCore.Qt.AlignRight)
        self.dob_lbl = QtWidgets.QLabel(self.frame)
        self.dob_lbl.setObjectName("dob_lbl")
        self.verticalLayout_3.addWidget(self.dob_lbl, 0, QtCore.Qt.AlignRight)
        self.gender_lbl = QtWidgets.QLabel(self.frame)
        self.gender_lbl.setObjectName("gender_lbl")
        self.verticalLayout_3.addWidget(self.gender_lbl, 0, QtCore.Qt.AlignRight)
        self.email_lbl = QtWidgets.QLabel(self.frame)
        self.email_lbl.setObjectName("email_lbl")
        self.verticalLayout_3.addWidget(self.email_lbl, 0, QtCore.Qt.AlignRight)
        self.pass_lbl = QtWidgets.QLabel(self.frame)
        self.pass_lbl.setObjectName("pass_lbl")
        self.verticalLayout_3.addWidget(self.pass_lbl, 0, QtCore.Qt.AlignRight)
        self.confirm_pass_lbl = QtWidgets.QLabel(self.frame)
        self.confirm_pass_lbl.setObjectName("confirm_pass_lbl")
        self.verticalLayout_3.addWidget(self.confirm_pass_lbl, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_5 = QtWidgets.QFrame(self.mid_frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.fn_input = QtWidgets.QLineEdit(self.frame_5)
        self.fn_input.setObjectName("fn_input")
        self.verticalLayout_4.addWidget(self.fn_input)
        self.ln_input = QtWidgets.QLineEdit(self.frame_5)
        self.ln_input.setObjectName("ln_input")
        self.verticalLayout_4.addWidget(self.ln_input)
        self.dob_input = QtWidgets.QDateEdit(self.frame_5)
        self.dob_input.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(3000, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dob_input.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1900, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dob_input.setCalendarPopup(True)
        self.dob_input.setObjectName("dob_input")
        self.verticalLayout_4.addWidget(self.dob_input)
        self.gender_input = QtWidgets.QComboBox(self.frame_5)
        self.gender_input.setObjectName("gender_input")
        self.gender_input.addItem("")
        self.gender_input.addItem("")
        self.gender_input.addItem("")
        self.verticalLayout_4.addWidget(self.gender_input)
        self.email_input = QtWidgets.QLineEdit(self.frame_5)
        self.email_input.setObjectName("email_input")
        self.verticalLayout_4.addWidget(self.email_input)
        self.pass_input = QtWidgets.QLineEdit(self.frame_5)
        self.pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_input.setObjectName("pass_input")
        self.verticalLayout_4.addWidget(self.pass_input)
        self.confirm_pass_input = QtWidgets.QLineEdit(self.frame_5)
        self.confirm_pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_pass_input.setObjectName("confirm_pass_input")
        self.verticalLayout_4.addWidget(self.confirm_pass_input)
        self.horizontalLayout.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.mid_frame)
        self.submit_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit_frame.sizePolicy().hasHeightForWidth())
        self.submit_frame.setSizePolicy(sizePolicy)
        self.submit_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.submit_frame.setToolTip("")
        self.submit_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.submit_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.submit_frame.setObjectName("submit_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.submit_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.submit_button = QtWidgets.QPushButton(self.submit_frame)
        self.submit_button.setObjectName("submit_button")
        self.verticalLayout_5.addWidget(self.submit_button, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.submit_frame)
        self.bottom_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_frame.sizePolicy().hasHeightForWidth())
        self.bottom_frame.setSizePolicy(sizePolicy)
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_frame.setObjectName("bottom_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.bottom_frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.account_lbl = QtWidgets.QLabel(self.bottom_frame)
        self.account_lbl.setObjectName("account_lbl")
        self.verticalLayout_6.addWidget(self.account_lbl, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.signin_lbl = QtWidgets.QLabel(self.bottom_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.signin_lbl.setFont(font)
        self.signin_lbl.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signin_lbl.setStyleSheet("color: rgb(52, 101, 164);")
        self.signin_lbl.setObjectName("signin_lbl")
        self.verticalLayout_6.addWidget(self.signin_lbl, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.bottom_frame)
        RegisterationWin.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegisterationWin)
        QtCore.QMetaObject.connectSlotsByName(RegisterationWin)
        self.submit_button.clicked.connect(self.submit_handle)

    def retranslateUi(self, RegisterationWin):
        _translate = QtCore.QCoreApplication.translate
        RegisterationWin.setWindowTitle(_translate("RegisterationWin", "Registeration FORM"))
        self.welcome_lbl.setText(_translate("RegisterationWin", "Welcome To"))
        self.label_6.setText(_translate("RegisterationWin", "Task Management System"))
        self.register_lbl.setText(_translate("RegisterationWin", "Registeration Form"))
        self.fn_lbl.setText(_translate("RegisterationWin", "First Name"))
        self.lb_lbl.setText(_translate("RegisterationWin", "Last Name"))
        self.dob_lbl.setText(_translate("RegisterationWin", "DOB"))
        self.gender_lbl.setText(_translate("RegisterationWin", "Gender"))
        self.email_lbl.setText(_translate("RegisterationWin", "E-mail"))
        self.pass_lbl.setText(_translate("RegisterationWin", "Password"))
        self.confirm_pass_lbl.setText(_translate("RegisterationWin", "Confirm Password"))
        self.dob_input.setDisplayFormat(_translate("RegisterationWin", "dd/MM/yyyy"))
        self.gender_input.setItemText(0, _translate("RegisterationWin", "Other"))
        self.gender_input.setItemText(1, _translate("RegisterationWin", "Male"))
        self.gender_input.setItemText(2, _translate("RegisterationWin", "Female"))
        self.submit_button.setText(_translate("RegisterationWin", "Submit"))
        self.account_lbl.setText(_translate("RegisterationWin", "Already Have an Account? "))
        self.signin_lbl.setText(_translate("RegisterationWin", "SignIn"))
