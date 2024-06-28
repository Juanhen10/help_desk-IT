from PySide6.QtCore import QSize, QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QFrame, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QSizePolicy, QStatusBar, QTableView, QToolButton, QWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(609, 480)
        MainWindow.setStyleSheet("QMainWindow {\n"
                                 "    border-radius: 15px;\n"
                                 "    text-align: center;\n"
                                 "}")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("QWidget {\n"
                                         "    border-radius: 15px;\n"
                                         "    background-color: rgba(27, 27, 27, 255);\n"
                                         "}")

        self.background = QFrame(self.centralwidget)
        self.background.setObjectName("background")
        self.background.setGeometry(20, 10, 571, 431)
        self.background.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)

        self.user_info = QFrame(self.background)
        self.user_info.setObjectName("user_info")
        self.user_info.setGeometry(10, 10, 551, 51)
        self.user_info.setStyleSheet("background-color: rgb(0, 216, 119);")
        self.user_info.setFrameShape(QFrame.StyledPanel)
        self.user_info.setFrameShadow(QFrame.Raised)

        self.perfil_img = QLabel(self.user_info)
        self.perfil_img.setObjectName("perfil_img")
        self.perfil_img.setGeometry(20, 20, 21, 16)
        self.perfil_img.setText("<html><head/><body><img   src=\"design/perfil\" ><p align=\"center\"></p></body></html>")

        self.nome_user = QLabel(self.user_info)
        self.nome_user.setObjectName("nome_user")
        self.nome_user.setGeometry(50, 10, 49, 16)
        self.nome_user.setText("NOME")

        self.departamento_user = QLabel(self.user_info)
        self.departamento_user.setObjectName("departamento_user")
        self.departamento_user.setGeometry(50, 30, 101, 16)
        self.departamento_user.setText("DEPARTAMENTO")

        self.departamento_user_2 = QLabel(self.user_info)
        self.departamento_user_2.setObjectName("departamento_user_2")
        self.departamento_user_2.setGeometry(200, 10, 181, 21)
        self.departamento_user_2.setText("ABERTURA DE CHAMADOS")

        self.Button_call = QToolButton(self.user_info)
        self.Button_call.setObjectName("Button_call")
        self.Button_call.setGeometry(500, 10, 22, 22)
        self.Button_call.setText("...")

        self.user_info_2 = QFrame(self.background)
        self.user_info_2.setObjectName("user_info_2")
        self.user_info_2.setGeometry(10, 70, 551, 351)
        self.user_info_2.setStyleSheet("background-color: rgb(0, 216, 119);")
        self.user_info_2.setFrameShape(QFrame.StyledPanel)
        self.user_info_2.setFrameShadow(QFrame.Raised)

        self.frame = QFrame(self.user_info_2)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(10, 30, 531, 31)
        self.frame.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(320, 10, 201, 20)
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QHBoxLayout.SetNoConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.ID_TXT_2 = QLabel(self.layoutWidget)
        self.ID_TXT_2.setObjectName("ID_TXT_2")
        self.ID_TXT_2.setStyleSheet("QLabel {\n"
                                    "    width: 5px;\n"
                                    "    color: black;\n"
                                    "}")

        self.horizontalLayout_2.addWidget(self.ID_TXT_2)

        self.DATA_TXT_2 = QLabel(self.layoutWidget)
        self.DATA_TXT_2.setObjectName("DATA_TXT_2")
        self.DATA_TXT_2.setMinimumSize(QSize(10, 0))
        self.DATA_TXT_2.setStyleSheet("color: rgb(0, 0, 0);")

        self.horizontalLayout_2.addWidget(self.DATA_TXT_2)

        self.TITLE_TXT_2 = QLabel(self.layoutWidget)
        self.TITLE_TXT_2.setObjectName("TITLE_TXT_2")
        self.TITLE_TXT_2.setStyleSheet("color: rgb(0, 0, 0);")

        self.horizontalLayout_2.addWidget(self.TITLE_TXT_2)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName("label")

        self.horizontalLayout_2.addWidget(self.label)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName("widget")
        self.widget.setGeometry(10, 10, 271, 18)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QHBoxLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.ID_TXT = QLabel(self.widget)
        self.ID_TXT.setObjectName("ID_TXT")
        self.ID_TXT.setStyleSheet("QLabel {\n"
                                  "    width: 5px;\n"
                                  "    color: black;\n"
                                  "}")

        self.horizontalLayout.addWidget(self.ID_TXT)

        self.DATA_TXT = QLabel(self.widget)
        self.DATA_TXT.setObjectName("DATA_TXT")
        self.DATA_TXT.setMinimumSize(QSize(10, 0))
        self.DATA_TXT.setStyleSheet("color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.DATA_TXT)

        self.TITLE_TXT = QLabel(self.widget)
        self.TITLE_TXT.setObjectName("TITLE_TXT")
        self.TITLE_TXT.setStyleSheet("color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.TITLE_TXT)

        self.lineEdit = QLineEdit(self.user_info_2)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setGeometry(20, 10, 171, 16)
        self.lineEdit.setStyleSheet("background-color: rgb(217, 217, 217);")

        self.tableView = QTableView(self.user_info_2)
        self.tableView.setObjectName("tableView")
        self.tableView.setGeometry(10, 70, 531, 271)
        self.tableView.setStyleSheet("background-color: rgb(217, 217, 217);")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        # Definindo o ícone da janela principal
        MainWindow.setWindowIcon(QIcon(u"webfoco.png"))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow"))
        self.perfil_img.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><img   src=\"design/perfil\" ><p align=\"center\"></p></body></html>"))
        self.nome_user.setText(QCoreApplication.translate("MainWindow", "NOME"))
        self.departamento_user.setText(QCoreApplication.translate("MainWindow", "DEPARTAMENTO"))
        self.departamento_user_2.setText(QCoreApplication.translate("MainWindow", "ABERTURA DE CHAMADOS"))
        self.Button_call.setText(QCoreApplication.translate("MainWindow", "..."))
        self.ID_TXT_2.setText(QCoreApplication.translate("MainWindow", "PRIORIDADE"))
        self.DATA_TXT_2.setText(QCoreApplication.translate("MainWindow", "TIPO "))
        self.TITLE_TXT_2.setText(QCoreApplication.translate("MainWindow", "STATUS"))
        self.label.setText(QCoreApplication.translate("MainWindow", "AÇÕES"))
        self.ID_TXT.setText(QCoreApplication.translate("MainWindow", "ID"))
        self.DATA_TXT.setText(QCoreApplication.translate("MainWindow", "DATA DO CHAMADO"))
        self.TITLE_TXT.setText(QCoreApplication.translate("MainWindow", "TITULO DO CHAMADO"))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()  # Aqui está correto - chamando show() na instância de QMainWindow
    sys.exit(app.exec())
