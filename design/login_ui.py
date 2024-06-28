from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt, QSize
from PySide6.QtGui import QFont, QPixmap, QIcon
from PySide6.QtWidgets import QApplication, QFrame, QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QStatusBar, QWidget, QHBoxLayout, QToolButton, QGraphicsDropShadowEffect, QMessageBox
import sys
from user_window import Ui_MainWindow as user_window
from PySide6.QtGui import QIntValidator
import webbrowser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(400, 400)
        MainWindow.setStyleSheet("QMainWindow{\n"
                                 " background-color: rgb(48, 47, 47);\n"
                                 " border-radius: 15px;\n"
                                 " text-align: center\n"
                                 "}")
        # Deixando trasparente 
        MainWindow.setWindowOpacity(0.9)  # Ajuste a opacidade conforme necessário
        MainWindow.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # Fundo transparente
        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Remove a borda da janela


        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setEnabled(True)
        
        
        # BACKGROUND (fundo)'
        self.background_frame = QFrame(self.centralwidget)
        self.background_frame.setObjectName("background_frame")
        self.background_frame.setGeometry(QRect(5, 5, 312, 312))
        self.background_frame.setAutoFillBackground(False)
        self.background_frame.setStyleSheet("QFrame {\n"
                                            " background-color: rgb(80, 80, 80);\n"
                                            " border-radius: 20px;\n"
                                            "}")
        self.background_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Shadow.Raised)


        # HOME #
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(10, 10, 301, 301))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("QFrame {\n"
                                 " background-color: rgb(255, 255, 255);\n"
                                 " border-radius: 15px;\n"
                                 "}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.layout = QVBoxLayout(self.frame)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centraliza o conteúdo verticalmente

        # Texto "SEJA BEM-VINDO" no topo
        self.layout_function = QHBoxLayout() # LAyout de organizar 
        #
        self.label = QLabel(self.frame)
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel{\n"
                                 " text-align: center;\n"
                                 " color: gray;\n"
                                 "}")
        self.layout_function.addWidget(self.label)
        # Botão de fechar 
        self.close_btn = QToolButton(self.frame)
        self.close_btn.setIcon(QIcon("design/icons/fechar.png"))
        self.close_btn.setIconSize(QSize(18, 18))
        self.close_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.close_btn.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.close_btn.setAutoRaise(True)
        self.close_btn.setAutoRaise(True)
        self.close_btn.setEnabled(True)
        # adicionando o botão
        self.layout_function.addWidget(self.close_btn)
        # adicionando no layout
        self.layout.addLayout(self.layout_function)
        # Imagem logo abaixo do texto
        self.imagem = QLabel(self.frame)
        self.imagem.setObjectName("imagem")
        self.imagem.setPixmap(QPixmap("design/icons/logo.png"))
        self.imagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.imagem)
        # login layout
        self.loginPin = QLineEdit(self.frame)
        self.loginPin.setObjectName("loginPin")
        self.loginPin.setAutoFillBackground(False)
        self.loginPin.setStyleSheet("QLineEdit {"
                                    "       border-radius: 5px;"
                                    "       height: 15px;"
                                    "       min-width: 200px;"  # Definindo largura mínima
                                    "       max-width: 150px;"  # Definindo largura máxima
                                    "       text-align: center"
                                    "}")
        self.loginPin.setValidator(QIntValidator())  # Define o validador para aceitar apenas inteiros
        self.layout.addWidget(self.loginPin,alignment=Qt.AlignmentFlag.AlignCenter)
        # Botão LOGIN
        self.pinBTN = QPushButton(self.frame)
        self.pinBTN.setObjectName("pinBTN")
        self.pinBTN.setEnabled(True)
        font = QFont()
        font.setBold(False)
        self.pinBTN.setFont(font)
        self.pinBTN.setCursor(Qt.CursorShape.PointingHandCursor)
        self.pinBTN.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.pinBTN.setStyleSheet("QPushButton {"
                                  "    background-color: rgb(27, 27, 27);"  # Cor de fundo do botão
                                  "    color: white;"  # Cor do texto
                                  "    border-radius: 5px;"
                                  "    min-width: 100px;"  # Definindo largura mínima
                                  "    max-width: 150px;"  # Definindo largura máxima
                                  "    height: 20px"
                                  "}"
                                  "QPushButton:hover {"
                                  "    background-color: rgba(0, 217, 113, 1);"
                                  "}"
                                  "QPushButton:pressed {"
                                  "    background-color: rgba(0, 217, 113, 0.5);"
                                  "}")
        self.layout.addWidget(self.pinBTN, alignment=Qt.AlignmentFlag.AlignCenter)  # Centraliza o botão dentro do layout

        # Conecta o sinal clicked do botão ao método login
        self.pinBTN.clicked.connect(self.login)
        self.desen_txt = QLabel(self.frame)
        self.desen_txt.setObjectName("desen_txt")
        self.desen_txt.setStyleSheet("QLabel{\n"
                                     " text-align: center;\n"
                                     " color: rgb(0, 0, 0);\n"
                                     "}")
        self.desen_txt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.desen_txt)


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # REDES SOCIAIS ICONS
        self.layout_social = QHBoxLayout()
        # Botão Facebook
        effect = QGraphicsDropShadowEffect()

        effect.setOffset(0, 0)

        effect.setBlurRadius(15)

        self.facebook_btn = QToolButton(self.frame)
        self.facebook_btn.setIcon(QIcon("design/icons/face.png"))
        self.facebook_btn.setIconSize(QSize(24, 24))
        self.facebook_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.facebook_btn.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.facebook_btn.setAutoRaise(True)  # Remove a borda ao redor do ícone
        self.facebook_btn.setEnabled(True)
        self.facebook_btn.setStyleSheet("QToolButton {"
                                         "    border: none;"  # Remove a borda
                                         "}"
                                         "QToolButton:hover{"
                                         "    background-color: rgba(0, 217, 113, 0.3);"
                                         "    border-radius: 50%"
                                         "}"
                                         "QToolButton:pressed {"
                                         "    background-color: rgba(0, 217, 113, 0.3);"
                                         "    padding-top: 5px;"
                                         "    padding-left: 5px"
                                         "}")
        self.facebook_btn.setGraphicsEffect(effect)
        self.layout_social.addWidget(self.facebook_btn)
        # Botão Instagram
        self.insta_btn = QToolButton(self.frame)
        self.insta_btn.setIcon(QIcon("design/icons/insta.png"))
        self.insta_btn.setIconSize(QSize(24, 24))
        self.insta_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.insta_btn.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.insta_btn.setAutoRaise(True)  # Remove a borda ao redor do ícone
        self.insta_btn.setEnabled(True)
        self.insta_btn.setStyleSheet("QToolButton {"
                                     "    border: none;"  # Remove a borda
                                     "}"
                                     "QToolButton:hover {"
                                     "    background-color: rgba(0, 217, 113, 0.3);"
                                     "}"
                                     "QToolButton:pressed {"
                                     "    background-color: rgba(0, 217, 113, 0.3);"
                                     "}")
        self.layout_social.addWidget(self.insta_btn)
        # linkedin
        self.likendin_btn = QToolButton(self.frame)
        self.likendin_btn.setIcon(QIcon("design/icons/like.png"))
        self.likendin_btn.setIconSize(QSize(24, 24))
        self.likendin_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.likendin_btn.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.likendin_btn.setAutoRaise(True)  # Remove a borda ao redor do ícone
        self.likendin_btn.setEnabled(True)
        self.likendin_btn.setStyleSheet("QToolButton {"
                                         "    border: none;"  # Remove a borda
                                         "}"
                                         "QToolButton:hover {"
                                         "    background-color: rgba(0, 217, 113, 0.3);"
                                         "}"
                                         "QToolButton:pressed {"
                                         "    background-color: rgba(0, 217, 113, 0.3);"
                                         "}")
        self.layout_social.addWidget(self.likendin_btn)
        # Youtube
        self.youtube_btn = QToolButton(self.frame)
        self.youtube_btn.setIcon(QIcon("design/icons/youtube.png"))
        self.youtube_btn.setIconSize(QSize(24, 24))
        self.youtube_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.youtube_btn.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.youtube_btn.setAutoRaise(True)  # Remove a borda ao redor do ícone
        self.youtube_btn.setEnabled(True)
        self.youtube_btn.setStyleSheet("QToolButton {"
                                         "    border: none;"  # Remove a borda
                                         "}"
                                         "QToolButton:hover {"
                                         "    background-color: rgba(0, 217, 113, 0.3);"
                                         "}"
                                         "QToolButton:pressed {"
                                         "    background-color: rgba(0, 217, 113, 0.3);"
                                         "}")
        self.layout_social.addWidget(self.youtube_btn)
        # Adiciona o layout de redes sociais ao layout principal
        self.layout.addLayout(self.layout_social)

         # Texto "Desenvolvido pela equipe de WB.P"
        self.desen_txt = QLabel(self.frame)
        self.desen_txt.setObjectName("desen_txt")
        self.desen_txt.setStyleSheet("QLabel{\n"
                                     " text-align: center;\n"
                                     " color: rgb(0, 0, 0);\n"
                                     "}")
        self.desen_txt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.desen_txt)


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    # Funcionalidades dos botões #
    # Conecta o sinal clicked do botão ao método login
        self.pinBTN.clicked.connect(self.login)
        self.close_btn.clicked.connect(MainWindow.close)  # Conecta o botão de fechar ao método close do MainWindow
        self.facebook_btn.clicked.connect(self.redes_sociais.facebook)
        self.likendin_btn.clicked.connect(self.redes_sociais.likendin)
        self.youtube_btn.clicked.connect(self.redes_sociais.youtube)
        self.insta_btn.clicked.connect(self.redes_sociais.insta)
        

    # Manipulação dos botões - clicagem dos links 
    class redes_sociais:
        def facebook():
            webbrowser.open("https://www.facebook.com/webfocomaispippe/")
        def likendin():
            webbrowser.open("https://br.linkedin.com/company/wbpgroup")
        def youtube():
            webbrowser.open("https://www.youtube.com/user/webfoco")
        def insta():
            webbrowser.open("https://www.instagram.com/webfocomaispippe/?igshid=YmMyMTA2M2Y%3D")
        def youtube():
            webbrowser.open("https://www.youtube.com/user/webfoco")
        
     # Este método verifica o PIN digitado e inicia a nova aplicação se o PIN estiver correto
    def login(self):
       # Este método verifica o PIN digitado e inicia a nova aplicação se o PIN estiver correto
        pin = self.loginPin.text().strip()
        if pin == "1234":  # Substitua por sua lógica de autenticação
            # Fechar a janela de login
            MainWindow.close()

            # Abrir a nova aplicação
            from user_window import Ui_MainWindow  # Supondo que Ui_MainWindow seja sua janela principal
            self.nova_app = QMainWindow()
            ui_main_window = Ui_MainWindow()
            ui_main_window.setupUi(self.nova_app)
            self.nova_app.show()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "SUPORTE WB.P", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family: 'Josefin Sans';\">SEJA BEM-VINDO AO WB.P SUPORTE!</span></p></body></html>", None))
        self.loginPin.setPlaceholderText(QCoreApplication.translate("MainWindow", "PIN", None))
        self.pinBTN.setText(QCoreApplication.translate("MainWindow", "LOGIN", None))
        self.desen_txt.setText(QCoreApplication.translate("MainWindow", 
                                                        "<html><head/><body><p align=\"center\"><span style=\"color:#949494; font-family:'Josefin Sans';\">Desenvolvido pela equipe da WB.P</span></p></body></html>", None))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
