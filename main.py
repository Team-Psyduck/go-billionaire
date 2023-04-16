from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Qt
from PySide2.QtAxContainer import QAxWidget
from pykiwoom.kiwoom import Kiwoom
from view import Ui_Dialog


class MainWindow(QMainWindow, Ui_Dialog, QAxWidget):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.kiwoom = Kiwoom()

        # self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.loginButton.clicked.connect(self.login)
        self.kiwoom.ocx.OnEventConnect.connect(self.event_connect)
        self.pwdButton.clicked.connect(self.getAccountData)

    def event_connect(self, err_code):
        if err_code == 0:
            print("로그인 성공")

            name = self.kiwoom.GetLoginInfo("USER_NAME")

            self.loginLabel.setAlignment(Qt.AlignRight)
            self.loginLabel.setText(f'{name}님 반갑습니다.')

            self.loginButton.hide()

    def login(self):
        kiwoom = self.kiwoom

        self.loginButton.setDisabled(True)
        kiwoom.CommConnect(block=True)
        self.loginButton.setDisabled(False)

        account_numbers = kiwoom.GetLoginInfo("ACCNO")
        self.accountList.addItems(account_numbers)

    def getAccountData(self):
        kiwoom = self.kiwoom
        print(self.accountList.currentText())
        print(len(self.pwdInput.text()))
        kiwoom.SetInputValue("계좌번호", self.accountList.currentText())
        # kiwoom.SetInputValue("비밀번호", self.pwdInput.text())
        kiwoom.SetInputValue("비밀번호입력매체구분", "00")
        kiwoom.SetInputValue("조회구분", "1")
        kiwoom.CommRqData("opw00004_req", "opw00004", 0, "2000")

        # 예수금 정보 출력하기
        deposit = kiwoom.GetCommData("opw00004", "", "d+2추정예수금", 0)
        print(f"예수금: {deposit}")


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()
