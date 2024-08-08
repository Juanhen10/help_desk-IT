# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adm_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QSizePolicy, QStatusBar, QToolButton,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(611, 474)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	Border-radius: 15px;\n"
"	text-align: center\n"
"	\n"
"\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	border-radius: 15px;\n"
"	background-color: rgba(27,27,27)\n"
"\n"
"\n"
"}")
        self.background = QFrame(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(20, 10, 571, 431))
        self.background.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.background.setFrameShape(QFrame.Shape.StyledPanel)
        self.background.setFrameShadow(QFrame.Shadow.Raised)
        self.user_info = QFrame(self.background)
        self.user_info.setObjectName(u"user_info")
        self.user_info.setGeometry(QRect(10, 10, 551, 51))
        self.user_info.setStyleSheet(u"background-color: rgb(0, 216, 119);")
        self.user_info.setFrameShape(QFrame.Shape.StyledPanel)
        self.user_info.setFrameShadow(QFrame.Shadow.Raised)
        self.perfil_img = QLabel(self.user_info)
        self.perfil_img.setObjectName(u"perfil_img")
        self.perfil_img.setGeometry(QRect(20, 20, 21, 16))
        self.nome_user = QLabel(self.user_info)
        self.nome_user.setObjectName(u"nome_user")
        self.nome_user.setGeometry(QRect(50, 10, 49, 16))
        self.departamento_user = QLabel(self.user_info)
        self.departamento_user.setObjectName(u"departamento_user")
        self.departamento_user.setGeometry(QRect(50, 30, 101, 16))
        self.departamento_user_2 = QLabel(self.user_info)
        self.departamento_user_2.setObjectName(u"departamento_user_2")
        self.departamento_user_2.setGeometry(QRect(200, 10, 181, 31))
        self.user_info_2 = QFrame(self.background)
        self.user_info_2.setObjectName(u"user_info_2")
        self.user_info_2.setGeometry(QRect(10, 70, 551, 351))
        self.user_info_2.setStyleSheet(u"background-color: rgb(0, 216, 119);")
        self.user_info_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.user_info_2.setFrameShadow(QFrame.Shadow.Raised)
        self.widget = QWidget(self.user_info_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 90, 551, 181))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.novo_chamado_btn = QToolButton(self.widget)
        self.novo_chamado_btn.setObjectName(u"novo_chamado_btn")

        self.horizontalLayout.addWidget(self.novo_chamado_btn)

        self.chamados_btn = QToolButton(self.widget)
        self.chamados_btn.setObjectName(u"chamados_btn")

        self.horizontalLayout.addWidget(self.chamados_btn)

        self.dashboard_btn = QToolButton(self.widget)
        self.dashboard_btn.setObjectName(u"dashboard_btn")

        self.horizontalLayout.addWidget(self.dashboard_btn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.perfil_img.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><img   src=\"design/perfil\" ><p align=\"center\"></p></body></html>", None))
        self.nome_user.setText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.departamento_user.setText(QCoreApplication.translate("MainWindow", u"DEPARTAMENTO", None))
        self.departamento_user_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">SUPORTE DE SISTEMAS</span></p></body></html>", None))
        self.novo_chamado_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.chamados_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.dashboard_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()  # Aqui está correto - chamando show() na instância de QMainWindow
    sys.exit(app.exec())
