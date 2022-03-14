from PyQt5.QtWidgets import QDialog


class CreateTaskDialog(QDialog):
    def __init__(self, parent, uic=None):
        super().__init__()

        self.window = uic.loadUi("create_task.ui", self)
        # Assigning Signals
        self.parent = parent
        self.ok_dialog_button.clicked.connect(self.ok_dialog_handle)
        self.window.closeEvent = self.close_parent

    def ok_dialog_handle(self):
        self.close()
        self.parent.close()
        task_win = CreateTaskDialog()
        task_win.name_label.setText(self.parent.login_user)
        task_win.show()

    def close_parent(self, event):
        self.parent.close()

