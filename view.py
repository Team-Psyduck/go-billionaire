# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'gobillionaireCOsWCI.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 480)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 20, 621, 451))
        self.tabWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.strategy_tab = QWidget()
        self.strategy_tab.setObjectName(u"strategy_tab")
        self.tabWidget.addTab(self.strategy_tab, "")
        self.asset_tab = QWidget()
        self.asset_tab.setObjectName(u"asset_tab")
        self.accountList = QComboBox(self.asset_tab)
        self.accountList.setObjectName(u"accountList")
        self.accountList.setEnabled(True)
        self.accountList.setGeometry(QRect(20, 20, 161, 22))
        self.pwdInput = QLineEdit(self.asset_tab)
        self.pwdInput.setObjectName(u"pwdInput")
        self.pwdInput.setGeometry(QRect(190, 20, 61, 20))
        self.pwdInput.setInputMask(u"")
        self.pwdInput.setValidator(QIntValidator())  # 숫자만 입력할 수 있도록 설정
        self.pwdInput.setMaxLength(4)
        self.pwdInput.setFrame(True)
        self.pwdInput.setEchoMode(QLineEdit.Password)
        self.pwdButton = QPushButton(self.asset_tab)
        self.pwdButton.setObjectName(u"pwdButton")
        self.pwdButton.setGeometry(QRect(260, 20, 31, 21))
        self.label = QLabel(self.asset_tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 25, 56, 12))
        self.assetView = QTableView(self.asset_tab)
        self.assetView.setObjectName(u"assetView")
        self.assetView.setGeometry(QRect(20, 60, 571, 341))
        self.tabWidget.addTab(self.asset_tab, "")
        self.auto_tab = QWidget()
        self.auto_tab.setObjectName(u"auto_tab")
        self.tabWidget.addTab(self.auto_tab, "")
        self.loginButton = QPushButton(Dialog)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(550, 10, 75, 23))
        self.loginLabel = QLabel(Dialog)
        self.loginLabel.setObjectName(u"loginLabel")
        self.loginLabel.setGeometry(QRect(460, 15, 161, 20))
        self.loginLabel.raise_()
        self.tabWidget.raise_()
        self.loginButton.raise_()

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", u"Dialog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.strategy_tab), QCoreApplication.translate("Dialog", u"\uc804\ub7b5\uc870\ud68c", None))
        self.pwdInput.setPlaceholderText(QCoreApplication.translate(
            "Dialog", u"\ube44\ubc00\ubc88\ud638", None))
        self.pwdButton.setText(
            QCoreApplication.translate("Dialog", u"OK", None))
        self.label.setText(QCoreApplication.translate(
            "Dialog", u"\ubcf4\uc720 \uae08\uc561: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.asset_tab), QCoreApplication.translate("Dialog", u"\uc790\uc0b0\uc870\ud68c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.auto_tab), QCoreApplication.translate("Dialog", u"\uc790\ub3d9\ub9e4\ub9e4", None))
        self.loginButton.setText(QCoreApplication.translate(
            "Dialog", u"\ud0a4\uc6c0 \ub85c\uadf8\uc778", None))
        self.loginLabel.setText("")
    # retranslateUi
