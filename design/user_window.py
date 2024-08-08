import sqlite3
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import QSize, Qt, QCoreApplication
from PySide6.QtGui import QPixmap, QIcon,QFont
from PySide6.QtWidgets import QApplication, QFrame, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QSizePolicy, QStatusBar, QTableView, QToolButton, QWidget, QStackedWidget
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QSizePolicy, QStackedWidget,
    QStatusBar, QToolButton, QTreeWidget, QTreeWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(904, 600)
        MainWindow.setStyleSheet("QMainWindow {\n"
                                 "    border-radius: 20px;\n"
                                 "    text-align: center;\n"
                                 "}")
        

        self.stacked_widget = QStackedWidget()
        # Deixando trasparente
        MainWindow.setWindowOpacity(1)
        MainWindow.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("QWidget {\n"
                                         "    border-radius: 0px;\n"
                                         "   \n"
                                         "}")

        self.background = QFrame(self.centralwidget)
        self.background.setObjectName("background")
        self.background.setGeometry(QRect(10, 10, 881, 585))
        self.background.setStyleSheet("background-color:#00D877;border-radius: 10px;")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        

        self.user_info = QFrame(self.background)
        self.user_info.setObjectName("user_info")
        self.user_info.setGeometry(QRect(10, 25, 900, 95))
        self.user_info.setStyleSheet("background-color: rgb(0, 216, 119);"
                                     "border-radius: 15")
        
        self.user_info.setFrameShape(QFrame.StyledPanel)
        self.user_info.setFrameShadow(QFrame.Raised)

        self.profile_img = QtWidgets.QLabel(self.user_info)
        self.profile_img.setObjectName("profile_img")
        self.profile_img.setGeometry(-6, -10, 95 , 80)  # X - Y - W - H (Largura e Altura iguais para um círculo)
        
        self.profile_img.setStyleSheet("""
            QLabel#profile_img {
                border-radius: 40px;  /* Metade do menor lado (80px) */
                
            }
        """)
        

         # Configuração da fonte personalizada
        fonte_titulo = QFont()
        fonte_titulo.setFamily("Josefin Sans")  # Substitua "NomeDaFonte" pelo nome da sua fonte
        fonte_titulo.setPointSize(12)

        fonte_textos = QFont()
        fonte_textos.setFamily("Josefin Sans SemiBold")  # Substitua "NomeDaFonte" pelo nome da sua fonte
        fonte_textos.setPointSize(10)

        fonte_subtextos = QFont()
        fonte_subtextos.setFamily("Josefin Sans SemiBold")  # Substitua "NomeDaFonte" pelo nome da sua fonte
        fonte_subtextos.setPointSize(5)

        # NOME DO USUARIO
        self.nome_user = QLabel(self.user_info)
        self.nome_user.setObjectName("nome_user")
        self.nome_user.setGeometry(65, 15, 100, 16)
        self.nome_user.setFont(fonte_textos)
        self.nome_user.setStyleSheet("color: black")
        
        # DEPARTAMENTOS
        self.departamento_user = QLabel(self.user_info)
        self.departamento_user.setObjectName("departamento_user")
        self.departamento_user.setGeometry(65, 35, 150, 15)
        self.departamento_user.setFont(fonte_subtextos)
        self.departamento_user.setStyleSheet("color: rgb(90, 90, 90)")

        # TÍTULO 
        self.title_chamado = QLabel(self.user_info)
        self.title_chamado.setObjectName("title_chamado")
        self.title_chamado.setGeometry(325, 10, 205, 25)
        self.title_chamado.setFont(fonte_titulo)
        self.title_chamado.setStyleSheet("color: black")
        # Versão do app texto
        self.vesion_title = QLabel(self.user_info)
        self.vesion_title.setObjectName("version_title")
        self.vesion_title.setGeometry(325, 35, 200, 25)
        self.vesion_title.setFont(fonte_textos)
        self.vesion_title.setStyleSheet("color: black")


        self.Button_call = QToolButton(self.user_info)
        self.Button_call.setIcon(QIcon("design/icons/mais--.png"))
        self.Button_call.setIconSize(QSize(100,100))
        self.Button_call.setCursor(Qt.CursorShape.PointingHandCursor)
        self.Button_call.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.Button_call.setObjectName("Button_call")
        self.Button_call.setGeometry(800, 16, 55, 30)


         # Botão de fechar 
        self.close_btn = QToolButton(self.background)
        self.close_btn.setIcon(QIcon("design/icons/fechar.png"))
        self.close_btn.setIconSize(QSize(45, 45))
        self.close_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.close_btn.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.close_btn.setGeometry(845,4,25,16)
        self.close_btn.setAutoRaise(True)
        self.close_btn.setEnabled(True)
        # minimizar
        self.mini_btn = QToolButton(self.background)
        self.mini_btn.setIcon(QIcon("design/icons/minimizar.png"))
        self.mini_btn.setIconSize(QSize(18,18))
        self.mini_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.mini_btn.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.mini_btn.setGeometry(810,6,35,12)
        self.mini_btn.setAutoRaise(True)
        self.mini_btn.setEnabled(True)
        
        #***************Configuração das telas*************
        self.painel_info = QStackedWidget(self.background)
        self.painel_info.setObjectName(u"painel_info")
        self.painel_info.setGeometry(QRect(10, 100, 861, 461))
        self.painel_info.setStyleSheet(u"background-color: #2D2D2D")

        

        self.user_window = QWidget()
        self.user_window.setObjectName(u"user_window")
        #***********Configuranção da tabela***************#
        # Paginas do sistema de chamados, onde os usuarios  terão acesso e abrirão seu chamado.
        self.system_table = QTreeWidget(self.user_window)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(6, Qt.AlignCenter)
        __qtreewidgetitem.setTextAlignment(5, Qt.AlignCenter)
        __qtreewidgetitem.setTextAlignment(4, Qt.AlignCenter)
        __qtreewidgetitem.setTextAlignment(3, Qt.AlignCenter)
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignCenter)
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignCenter)
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter)
        self.system_table.setHeaderItem(__qtreewidgetitem)
        self.system_table.setObjectName(u"sistema_chamado")
        self.system_table.setGeometry(QRect(0, 0, 861, 461))
        # Ajustar a largura das colunas
        self.system_table.setColumnWidth(0, 50)  # Número
        self.system_table.setColumnWidth(1, 100)  # Data
        self.system_table.setColumnWidth(2, 200)  # Título do chamado
        self.system_table.setColumnWidth(3, 150)  # Tipo do chamado
        self.system_table.setColumnWidth(4, 100)  # PRIORIDADE
        self.system_table.setColumnWidth(5, 150)  # RESPONSAVEL
        self.system_table.setColumnWidth(6, 100)  # Status

         #Definir a fonte
        font = QFont("Josefin Sans SemiBold", 10)  # Aqui você pode definir a fonte que preferir

        # Aplicar a fonte ao headerItem
        header_item = self.system_table.headerItem()
        for col in range(header_item.columnCount()):
            header_item.setFont(col, font)

        # Aplicar a fonte aos itens da tabela (se houver itens na tabela)
        for i in range(self.system_table.topLevelItemCount()):
            item = self.system_table.topLevelItem(i)
            for col in range(item.columnCount()):
                item.setFont(col, font)

        self.painel_info.addWidget(self.user_window)
        # Tela de administração, onde os administradores do TI terão acesso, ou seja só quem tem o PIN de administrador verá essa teça
        
        self.window_adm = QWidget()
        self.window_adm.setObjectName(u"window_adm")
        self.home_adm = QFrame(self.window_adm)
        self.home_adm.setObjectName(u"home_adm")
        self.home_adm.setGeometry(QRect(20, 40, 831, 361))
        self.home_adm.setStyleSheet(u"background-color: #2D2D2D")
        self.home_adm.setFrameShape(QFrame.Shape.StyledPanel)
        self.home_adm.setFrameShadow(QFrame.Shadow.Raised)
        # botão de chamados, onde vamos manipular os chamados dos usuarios, ou seja os administradores mexerão no banco de dados, vão poder colocar a prioridade, o status, responsavel, etc
        self.call_btn = QToolButton(self.home_adm)
        self.call_btn.setObjectName(u"call_btn")
        self.call_btn.setMaximumSize(QSize(174, 166))
        self.call_btn.setStyleSheet(u"background-color: #00D877;"
                                    "color: black")
        # botão de dashboard, vai mostrar um dashboard de todos os chamados, das areas, de quem fez, etc. Além de baixar relatorios, tanto de aquivos .csv quanto arquivos .pdf
        self.dashboard_btn = QToolButton(self.home_adm)
        self.dashboard_btn.setObjectName(u"dashboard_btn")
        self.dashboard_btn.setMaximumSize(QSize(174, 166))
        self.dashboard_btn.setStyleSheet(u"background-color: #00D877;"
                                         "color: black""")
        
        # aqui vai ir para mesma tela que do usuario padrão, onde pode abrir um chamado.
        self.new_call_btn = QToolButton(self.home_adm)
        self.new_call_btn.setObjectName(u"new_call_btn")
        self.new_call_btn.setMaximumSize(QSize(174, 166))
        self.new_call_btn.setStyleSheet(u"background-color: #00D877;"
                                        "color: black")
        

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)

        # Definindo o ícone da janela principal
        MainWindow.setWindowIcon(QIcon(u"webfoco.png"))
        
        # Ações dos botões
        self.close_btn.clicked.connect(MainWindow.close)
        self.mini_btn.clicked.connect(MainWindow.showMinimized)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.departamento_user.setText(QCoreApplication.translate("MainWindow", 
                                                        "<html><head/><body><p align=\"center\"><span style=\"color: #E0E0E0; font-family:'Josefin Sans SemiBold';\">DEPARTAMENTO</span></p></body></html>", None))
        self.nome_user.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">TextLabel</span></p></body></html>", None))
        self.title_chamado.setText(QCoreApplication.translate("MainWindow", 
                                                        "<html><head/><body><p align=\"center\"><span style=\"color: black; font-family:'Josefin Sans SemiBold';\">ABERTURA DE CHAMADO</span></p></body></html>", None))
        self.profile_img.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><img src=\"design/profile\" ><p align=\"center\"></p></body></html>"))
        self.vesion_title.setText(QCoreApplication.translate("MainWindow", 
                                                        "<html><head/><body><p align=\"center\"><span style=\"color: #E0E0E0; font-family:'Josefin Sans SemiBold';\">versão 1.0.0</span></p></body></html>", None))

        ___qtreewidgetitem = self.system_table.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"N\u00ba", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"DATA", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"T\u00cdTULO DO CHAMADO", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"TIPO DO CHAMADO", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"PRIORIDADE", None))
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"RESPONSÁVEL", None))
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"STATUS", None));
        self.call_btn.setText(QCoreApplication.translate("MainWindow", u"CHAMADOS ", None))
        self.dashboard_btn.setText(QCoreApplication.translate("MainWindow", u"NOVO CHAMADO", None))
        self.new_call_btn.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
    # retranslateUi
        
        
    def load_user_data(self, pin):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nome, departamento, imagem FROM users WHERE pin=?", (pin,))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            nome, departamento, imagem = result
            self.nome_user.setText(nome)
            self.departamento_user.setText(departamento)
            self.set_image(imagem)
            
        else:
            print("Usuário não encontrado.")
        
    def set_image(self, imagem):
        pixmap = QtGui.QPixmap()
        
        if pixmap.loadFromData(imagem):  # Carrega a imagem dos dados
            # Redimensiona a imagem
            pixmap = pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        
            # Define o pixmap no QLabel
            self.profile_img.setPixmap(pixmap)
            self.profile_img.setScaledContents(True)
        else:
            print("Failed to load image from data")
        
    def open_call_window(): 
        pass


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()  # Aqui está correto - chamando show() na instância de QMainWindow
    sys.exit(app.exec())



