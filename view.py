# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'gobillionairejpMPkk.ui'
##
# Created by: Qt User Interface Compiler version 6.2.4
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
                               QTabWidget, QWidget)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 480)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 621, 461))
        self.tabWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.strategy_tab = QWidget()
        self.strategy_tab.setObjectName(u"strategy_tab")
        self.tabWidget.addTab(self.strategy_tab, "")
        self.asset_tab = QWidget()
        self.asset_tab.setObjectName(u"asset_tab")
        self.tabWidget.addTab(self.asset_tab, "")
        self.auto_tab = QWidget()
        self.auto_tab.setObjectName(u"auto_tab")
        self.loginButton = QPushButton(self.auto_tab)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(530, 10, 75, 23))
        self.tabWidget.addTab(self.auto_tab, "")

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(2)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", u"Dialog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.strategy_tab), QCoreApplication.translate("Dialog", u"\uc804\ub7b5\uc870\ud68c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.asset_tab), QCoreApplication.translate("Dialog", u"\uc790\uc0b0\uc870\ud68c", None))
        self.loginButton.setText(QCoreApplication.translate(
            "Dialog", u"\ud0a4\uc6c0 \ub85c\uadf8\uc778", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.auto_tab), QCoreApplication.translate("Dialog", u"\uc790\ub3d9\ub9e4\ub9e4", None))
    # retranslateUi
