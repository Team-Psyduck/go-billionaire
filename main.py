from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtAxContainer import QAxWidget
from view import Ui_Dialog


class MainWindow(QMainWindow, Ui_Dialog, QAxWidget):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.loginButton.clicked.connect(self.login)

    def login(self):
        return self.kiwoom.dynamicCall("CommConnect()")


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()
