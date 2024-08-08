from PySide6.QtWidgets import QToolButton, QStatusBar,QHBoxLayout ,QSizePolicy,QFrame,QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QTextEdit, QApplication, QMainWindow
from PySide6.QtCore import QDateTime, QRect, QSize, QMetaObject ,QCoreApplication, Qt
from PySide6.QtGui import QPixmap, QIcon,QFont
import requests


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
            if not MainWindow.objectName():
                MainWindow.setObjectName(u"MainWindow")
            MainWindow.resize(456, 464)
            MainWindow.setStyleSheet("QMainWindow{\n"
                                 " background-color: #00D877;\n"
                                 " border-radius: 25px;\n"
                                 " text-align: center\n"
                                 "}")
            # Deixando trasparente 
            MainWindow.setWindowOpacity(1)  # Ajuste a opacidade conforme necessário
            MainWindow.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # Fundo transparente
            MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Remove a borda da janela

            self.centralwidget = QWidget(MainWindow)
            self.centralwidget.setObjectName(u"centralwidget")
            self.centralwidget.setEnabled(True)
            self.centralwidget.setStyleSheet("QFrame {\n"
                                            " background-color: #00D877;\n"
                                            " border-radius: 20px;\n"
                                            "}")


            self.background = QFrame(self.centralwidget)
            self.background.setObjectName(u"background")
            self.background.setGeometry(QRect(10, 20, 441, 431))
            self.background.setAutoFillBackground(False)
            self.background.setStyleSheet("QFrame {\n"
                                            " background-color: #00D877;\n"
                                            " border-radius: 20px;\n"
                                            "}")
            self.background.setFrameShape(QFrame.Shape.StyledPanel)
            self.background.setFrameShadow(QFrame.Shadow.Raised)

             # Botão de fechar 
            self.close_btn = QToolButton(self.background)
            self.close_btn.setIcon(QIcon("design/icons/fechar.png"))
            self.close_btn.setIconSize(QSize(45, 45))
            self.close_btn.setCursor(Qt.CursorShape.PointingHandCursor)
            self.close_btn.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
            self.close_btn.setGeometry(390,4,35,16)
            self.close_btn.setAutoRaise(True)
            self.close_btn.setEnabled(True)
            


            self.label = QFrame(self.background)
            self.label.setObjectName(u"label")
            self.label.setGeometry(QRect(15, 20, 411, 391))
            self.label.setStyleSheet(u"background-color: #2D2D2D")
            self.label.setFrameShape(QFrame.Shape.StyledPanel)
            self.label.setFrameShadow(QFrame.Shadow.Raised)
            
            self.layoutWidget = QWidget(self.label)
            self.layoutWidget.setObjectName(u"layoutWidget")
            self.layoutWidget.setGeometry(QRect(20, 130, 258, 22))
            self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget)
            self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
            self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
            #********************* FORMULÁRIO ******************************#
            self.type_label = QLabel(self.layoutWidget)
            self.type_label.setObjectName(u"type_label")
            self.type_label.setStyleSheet(u"color: white;\n"
                                        "font: 600 italic 9pt \"Josefin Sans SemiBold\";")

            self.horizontalLayout_4.addWidget(self.type_label)

            self.type_input = QComboBox(self.layoutWidget)
            self.type_input.addItem("")
            self.type_input.addItem("")
            self.type_input.addItem("")
            self.type_input.addItem("")
            self.type_input.setObjectName(u"type_input")
            self.type_input.setStyleSheet(u"background-color: #1E1E1E;\n"
                                             "font: 600 italic 7pt \"Josefin Sans SemiBold\";")

            self.horizontalLayout_4.addWidget(self.type_input)

            self.description_label = QLabel(self.label)
            self.description_label.setObjectName(u"description_label")
            self.description_label.setGeometry(QRect(20, 170, 72, 16))
            self.description_label.setStyleSheet(u"color: white;\n"
                                              "font: 600 italic 9pt \"Josefin Sans SemiBold\";")
            self.layoutWidget_2 = QWidget(self.label)
            self.layoutWidget_2.setObjectName(u"layoutWidget_2")
            self.layoutWidget_2.setGeometry(QRect(21, 71, 381, 24))
            self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget_2)
            self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
            self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
            self.title_label = QLabel(self.layoutWidget_2)
            self.title_label.setObjectName(u"title_label")
            self.title_label.setStyleSheet(u"color: white;\n"
                                          "font: 600 italic 9pt \"Josefin Sans SemiBold\";")

            self.horizontalLayout_3.addWidget(self.title_label)

            self.title_input = QLineEdit(self.layoutWidget_2)
            self.title_input.setObjectName(u"title_input")
            self.title_input.setStyleSheet(u"background-color: #1E1E1E")

            self.horizontalLayout_3.addWidget(self.title_input)

            self.layoutWidget_3 = QWidget(self.label)
            self.layoutWidget_3.setObjectName(u"layoutWidget_3")
            self.layoutWidget_3.setGeometry(QRect(70, 320, 281, 56))
            self.verticalLayout = QVBoxLayout(self.layoutWidget_3)
            self.verticalLayout.setObjectName(u"verticalLayout")
            self.verticalLayout.setContentsMargins(0, 0, 0, 0)
            self.submit_button = QPushButton(self.layoutWidget_3)
            self.submit_button.setObjectName(u"submit_button")
            self.submit_button.setStyleSheet("QPushButton {"
                                    "font: 600 italic 9pt \"Josefin Sans SemiBold\";"
                                  "    background-color: rgb(27, 27, 27);"  # Cor de fundo do botão
                                  "    color: white;"  # Cor do texto
                                  "    border-radius: 5px;"
                                  "    min-width: 250px;"  # Definindo largura mínima
                                  "    max-width: 300;"  # Definindo largura máxima
                                  "    height: 20px"
                                  "}"
                                  "QPushButton:hover {"
                                  "    background-color: rgba(0, 217, 113, 1);"
                                  "}"
                                  "QPushButton:pressed {"
                                  "    background-color: rgba(0, 217, 113, 0.5);"
                                  
                                  "}")
            

            self.verticalLayout.addWidget(self.submit_button)

            self.cancel_button = QPushButton(self.layoutWidget_3)
            self.cancel_button.setObjectName(u"cancel_button")
            self.cancel_button.setStyleSheet("QPushButton {"
                                    "font: 600 italic 9pt \"Josefin Sans SemiBold\";"
                                  "    background-color: rgb(27, 27, 27);"  # Cor de fundo do botão
                                  "    color: white;"  # Cor do texto
                                  "    border-radius: 5px;"
                                  "    min-width: 250Tpx;"  # Definindo largura mínima
                                  "    max-width: 300;"  # Definindo largura máxima
                                  "    height: 20px"
                                  "}"
                                  "QPushButton:hover {"
                                  "    background-color: rgba(0, 217, 113, 1);"
                                  "}"
                                  "QPushButton:pressed {"
                                  "    background-color: rgba(0, 217, 113, 0.5);"
                                  
                                  "}")

            self.verticalLayout.addWidget(self.cancel_button)

            self.layoutWidget_4 = QWidget(self.label)
            self.layoutWidget_4.setObjectName(u"layoutWidget_4")
            self.layoutWidget_4.setGeometry(QRect(60, 0, 301, 61))
            self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_4)
            self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
            self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
            self.margen_2 = QLabel(self.layoutWidget_4)
            self.margen_2.setObjectName(u"margen_2")
            self.margen_2.setEnabled(False)
            self.margen_2.setStyleSheet(u"font: 600 italic 9pt \"Josefin Sans SemiBold\";\n"
                                                                             "color: black")

            self.horizontalLayout_2.addWidget(self.margen_2)

            self.title_txt = QLabel(self.layoutWidget_4)
            self.title_txt.setObjectName(u"title_txt")
            self.title_txt.setEnabled(True)
            self.title_txt.setStyleSheet(u"font: 600 italic 9pt \"Josefin Sans SemiBold\";\n"
                                                                                 "color: white")

            self.horizontalLayout_2.addWidget(self.title_txt)

            self.margen = QLabel(self.layoutWidget_4)
            self.margen.setObjectName(u"margen")
            self.margen.setEnabled(False)

            self.horizontalLayout_2.addWidget(self.margen)

            self.description_input = QTextEdit(self.label)
            self.description_input.setObjectName(u"description_input")
            self.description_input.setGeometry(QRect(20, 190, 381, 111))
            self.description_input.setStyleSheet(u"background-color: #1E1E1E")


            self.layoutWidget_5 = QWidget(self.label)
            self.layoutWidget_5.setObjectName(u"layoutWidget_5")
            self.layoutWidget_5.setGeometry(QRect(20, 100, 381, 24))
            self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_5)
            self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
            self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
            self.responsible_label = QLabel(self.layoutWidget_5)
            self.responsible_label.setObjectName(u"responsible_label")
            self.responsible_label.setStyleSheet(u"color: white;\n"
                                                 "font: 600 italic 9pt \"Josefin Sans SemiBold\";")

            self.horizontalLayout_5.addWidget(self.responsible_label)

            self.responsible_input = QLineEdit(self.layoutWidget_5)
            self.responsible_input.setObjectName(u"responsible_input")
            self.responsible_input.setStyleSheet(u"background-color: #1E1E1E")

            self.horizontalLayout_5.addWidget(self.responsible_input)

            self.widget = QWidget(self.label)
            self.widget.setObjectName(u"widget")
            self.widget.setGeometry(QRect(281, 130, 123, 22))
            self.horizontalLayout = QHBoxLayout(self.widget)
            self.horizontalLayout.setObjectName(u"horizontalLayout")
            self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.priority_label = QLabel(self.widget)
            self.priority_label.setObjectName(u"priority_label")
            self.priority_label.setStyleSheet(u"color: white;\n"
                                             "font: 600 italic 7pt \"Josefin Sans SemiBold\";")

            self.horizontalLayout.addWidget(self.priority_label)

            self.priority_input = QComboBox(self.widget)
            self.priority_input.addItem("")
            self.priority_input.addItem("")
            self.priority_input.addItem("")
            self.priority_input.setObjectName(u"priority_input")
            self.priority_input.setStyleSheet(u"background-color: #1E1E1E;\n"
                                                 "font: 600 italic 7pt \"Josefin Sans SemiBold\";")

            self.horizontalLayout.addWidget(self.priority_input)

            MainWindow.setCentralWidget(self.centralwidget)
            self.statusbar = QStatusBar(MainWindow)
            self.statusbar.setObjectName(u"statusbar")
            MainWindow.setStatusBar(self.statusbar)

            self.retranslateUi(MainWindow)

            QMetaObject.connectSlotsByName(MainWindow)
        # setupUi
        # Ações dos botões.
            self.cancel_button.clicked.connect(MainWindow.close)
            self.close_btn.clicked.connect(MainWindow.close)
            self.submit_button.clicked.connect(self.submit_call)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.type_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">TIPO DO CHAMADO:</p></body></html>", None))
        self.type_input.setItemText(0, QCoreApplication.translate("MainWindow", u"SISTEMA", None))
        self.type_input.setItemText(1, QCoreApplication.translate("MainWindow", u"INFRA", None))
        self.type_input.setItemText(2, QCoreApplication.translate("MainWindow", u"CRIA\u00c7\u00c3O DE USU\u00c1RIO ", None))
        self.type_input.setItemText(3, QCoreApplication.translate("MainWindow", u"DESENVOLVIMENTO", None))

        self.description_label.setText(QCoreApplication.translate("MainWindow", u"DESCRICÃO:", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"T\u00cdTULO DO CHAMADO:", None))
        self.title_input.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR CHAMADO", None))
        self.cancel_button.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.margen_2.setText("")
        self.title_txt.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">NOVO CHAMADO</p></body></html>", None))
        self.margen.setText("")
        self.responsible_label.setText(QCoreApplication.translate("MainWindow", u"RESPONS\u00c1VEL:", None))
        self.priority_label.setText(QCoreApplication.translate("MainWindow", u"PRIORIDADE:", None))
        self.priority_input.setItemText(0, QCoreApplication.translate("MainWindow", u"BAIXA", None))
        self.priority_input.setItemText(1, QCoreApplication.translate("MainWindow", u"M\u00c9DIA", None))
        self.priority_input.setItemText(2, QCoreApplication.translate("MainWindow", u"ALTA", None))

    # retranslateUi

    def submit_call(self):
        title = self.title_input.text()
        description = self.description_input.toPlainText()
        call_type = self.type_input.currentText()
        priority = self.priority_input.currentText()
        responsible = self.responsible_input.text()
        created_by = "Usuário Atual"  # Aqui você colocará o nome do usuário atual
        current_date = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")

        data = {
            "title": title,
            "description": description,
            "type": call_type,
            "priority": priority,
            "responsible": responsible,
            "status": "Aberto",
            "created_by": created_by,
            "created_at": current_date,
            "sla_time": 0,  # Será calculado no servidor
            "archived_at": None  # Data de arquivamento será preenchida posteriormente
        }

        url = "http://localhost:5000/register_call"
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Chamado registrado com sucesso!")
        else:
            print("Erro ao registrar chamado.")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()  # Aqui está correto - chamando show() na instância de QMainWindow
    sys.exit(app.exec())

