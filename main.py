from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide2.QtCore import Qt
from PySide2.QtAxContainer import QAxWidget
from pykiwoom.kiwoom import Kiwoom
from view import Ui_Dialog


class MainWindow(QMainWindow, Ui_Dialog, QAxWidget):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.kiwoom = Kiwoom()

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

        self.kiwoom.ocx.dynamicCall(
            "KOA_Functions(QString, QString)", "ShowAccountWindow", "")

    def getAccountData(self):
        kiwoom = self.kiwoom
        print(self.accountList.currentText())

        # 예수금 정보 출력하기
        df = kiwoom.block_request("opw00001",
                                  계좌번호=self.accountList.currentText(),
                                  비밀번호="",
                                  비밀번호입력매체구분="00",
                                  조회구분=2,
                                  output="예수금상세현황",
                                  next=0)

        deposit = int(df['예수금'][0])
        self.depositLabel_2.setText(f'{deposit:,}')

        # 계좌평가결과 출력하기
        df = kiwoom.block_request("opw00018",
                                  계좌번호=self.accountList.currentText(),
                                  비밀번호="",
                                  비밀번호입력매체구분="00",
                                  조회구분=2,
                                  output="계좌평가결과",
                                  next=0)

        li = ['종목명', '매입금액', '평가금액', '평가손익금액', '수익률(%)']

        for i, s in enumerate(li):
            name = QTableWidgetItem(s)
            self.assetTable.setHorizontalHeaderItem(i, name)

        li = ['총매입금액', '총평가금액', '총평가손익금액', '총수익률(%)']

        total = QTableWidgetItem("총합")
        total.setTextAlignment(Qt.AlignCenter)
        self.assetTable.setItem(0, 0, total)
        for i, s in enumerate(li, start=1):
            num = QTableWidgetItem(str(float(df[s][0])))
            num.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.assetTable.setItem(0, i, num)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()
