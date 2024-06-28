# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QSizePolicy, QStatusBar, QTableView, QToolButton,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(609, 480)
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
        self.departamento_user_2.setGeometry(QRect(200, 10, 181, 21))
        self.Button_call = QToolButton(self.user_info)
        self.Button_call.setObjectName(u"Button_call")
        self.Button_call.setGeometry(QRect(500, 10, 22, 22))
        self.user_info_2 = QFrame(self.background)
        self.user_info_2.setObjectName(u"user_info_2")
        self.user_info_2.setGeometry(QRect(10, 70, 551, 351))
        self.user_info_2.setStyleSheet(u"background-color: rgb(0, 216, 119);")
        self.user_info_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.user_info_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame = QFrame(self.user_info_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 30, 531, 31))
        self.frame.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(320, 10, 201, 20))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ID_TXT_2 = QLabel(self.layoutWidget)
        self.ID_TXT_2.setObjectName(u"ID_TXT_2")
        self.ID_TXT_2.setStyleSheet(u"QLabel{\n"
"	widht: 5px;\n"
"	color: black\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.ID_TXT_2)

        self.DATA_TXT_2 = QLabel(self.layoutWidget)
        self.DATA_TXT_2.setObjectName(u"DATA_TXT_2")
        self.DATA_TXT_2.setMinimumSize(QSize(10, 0))
        self.DATA_TXT_2.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_2.addWidget(self.DATA_TXT_2)

        self.TITLE_TXT_2 = QLabel(self.layoutWidget)
        self.TITLE_TXT_2.setObjectName(u"TITLE_TXT_2")
        self.TITLE_TXT_2.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_2.addWidget(self.TITLE_TXT_2)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 271, 18))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ID_TXT = QLabel(self.widget)
        self.ID_TXT.setObjectName(u"ID_TXT")
        self.ID_TXT.setStyleSheet(u"QLabel{\n"
"	widht: 5px;\n"
"	color: black\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.ID_TXT)

        self.DATA_TXT = QLabel(self.widget)
        self.DATA_TXT.setObjectName(u"DATA_TXT")
        self.DATA_TXT.setMinimumSize(QSize(10, 0))
        self.DATA_TXT.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.DATA_TXT)

        self.TITLE_TXT = QLabel(self.widget)
        self.TITLE_TXT.setObjectName(u"TITLE_TXT")
        self.TITLE_TXT.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.TITLE_TXT)

        self.lineEdit = QLineEdit(self.user_info_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 10, 171, 16))
        self.lineEdit.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.tableView = QTableView(self.user_info_2)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 70, 531, 271))
        self.tableView.setStyleSheet(u"background-color: rgb(217, 217, 217);")
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
        self.departamento_user_2.setText(QCoreApplication.translate("MainWindow", u"ABERTURA DE CHAMADOS", None))
        self.Button_call.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ID_TXT_2.setText(QCoreApplication.translate("MainWindow", u"PRIORIDADE", None))
        self.DATA_TXT_2.setText(QCoreApplication.translate("MainWindow", u"TIPO ", None))
#if QT_CONFIG(whatsthis)
        self.TITLE_TXT_2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">hkj</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.TITLE_TXT_2.setText(QCoreApplication.translate("MainWindow", u"STATUS", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"A\u00c7\u00d5ES", None))
        self.ID_TXT.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.DATA_TXT.setText(QCoreApplication.translate("MainWindow", u"DATA DO CHAMADO", None))
#if QT_CONFIG(whatsthis)
        self.TITLE_TXT.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">hkj</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.TITLE_TXT.setText(QCoreApplication.translate("MainWindow", u"TITULO DO CHAMADO", None))
    # retranslateUi

